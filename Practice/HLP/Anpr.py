import os
import random

import numpy as np
import pandas as pd
import pennylane as qml
import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.metrics import classification_report, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from torch.utils.data import DataLoader, TensorDataset


# ======================================================
# SETTINGS
# ======================================================

n_qubits = 6
n_layers = 3
n_classes = 3

EPOCHS = 35
BATCH_SIZE = 32

ENTANGLEMENT = None
DATASET = None

# PyTorch GPU: classical neural-network layers use CUDA.
torch_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"PyTorch device: {torch_device}")

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
else:
    raise RuntimeError(
        "CUDA GPU was not found. Install the CUDA-enabled PyTorch package."
    )

# Native Windows fallback:
# Quantum circuit runs on CPU, while PyTorch layers run on GPU.
q_device = qml.device("lightning.qubit", wires=n_qubits)
print("Quantum device: lightning.qubit (CPU)")


# ======================================================
# REPRODUCIBILITY
# ======================================================

def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)

    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# ======================================================
# DATA LOADING
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_dataset(dataset_name):
    """
    dataset_name example: FD001
    Expected file name: train_FD001.txt
    """

    data_path = os.path.join(BASE_DIR, f"train_{dataset_name}.txt")

    print(f"Loading {dataset_name} dataset from {data_path} ...")

    df = pd.read_csv(data_path, sep=" ", header=None)
    df = df.dropna(axis=1)

    # Remaining Useful Life
    df["RUL"] = df.groupby(0)[1].transform("max") - df[1]

    def label_rul(rul):
        if rul > 80:
            return 0       # Healthy
        elif rul > 30:
            return 1       # Degrading
        return 2           # Failure

    df["label"] = df["RUL"].apply(label_rul)

    features = df.drop(columns=[0, 1, "RUL", "label"])
    labels = df["label"]

    print(f"Total samples: {len(features)}")
    print(
        f"Class distribution: "
        f"{labels.value_counts().sort_index().to_dict()}\n"
    )

    return features, labels


# ======================================================
# CLASSICAL FEATURE EXTRACTOR — GPU
# ======================================================

class FeatureExtractor(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, n_qubits)
        )

    def forward(self, x):
        return self.net(x)


# ======================================================
# ENTANGLEMENT FUNCTIONS
# ======================================================

def linear_entanglement():
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])


def ring_entanglement():
    for i in range(n_qubits):
        qml.CNOT(wires=[i, (i + 1) % n_qubits])


def full_entanglement():
    for i in range(n_qubits):
        for j in range(i + 1, n_qubits):
            qml.CNOT(wires=[i, j])


# ======================================================
# QUANTUM CIRCUIT — CPU
# ======================================================

@qml.qnode(q_device, interface="torch")
def quantum_circuit(inputs, weights):

    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)

    for layer in range(n_layers):

        for i in range(n_qubits):
            qml.RX(weights[layer, i, 0], wires=i)
            qml.RZ(weights[layer, i, 1], wires=i)

        if ENTANGLEMENT == "linear":
            linear_entanglement()

        elif ENTANGLEMENT == "ring":
            ring_entanglement()

        elif ENTANGLEMENT == "full":
            full_entanglement()

        # Data re-uploading
        for i in range(n_qubits):
            qml.RY(inputs[i], wires=i)

    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]


# ======================================================
# HYBRID QUANTUM-CLASSICAL MODEL
# ======================================================

class HybridModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        self.feature_extractor = FeatureExtractor(input_dim)

        self.q_params = nn.Parameter(
            0.01 * torch.randn(n_layers, n_qubits, 2)
        )

        self.classical_head = nn.Sequential(
            nn.Linear(n_qubits, 12),
            nn.ReLU(),
            nn.Linear(12, n_classes)
        )

    def forward(self, x):
        # Runs on GPU
        latent = torch.tanh(self.feature_extractor(x))
        latent_scaled = (latent + 1) * (torch.pi / 2)

        # PennyLane lightning.qubit runs on CPU.
        # Copy each sample and quantum parameters to CPU for the circuit.
        q_weights_cpu = self.q_params.cpu()
        q_outputs = []

        for sample in latent_scaled:
            q_out = torch.stack(
                quantum_circuit(sample.cpu(), q_weights_cpu)
            )

            # Return quantum outputs to GPU for the classification head.
            q_outputs.append(q_out.to(x.device))

        q_outputs = torch.stack(q_outputs).float()

        # Runs on GPU
        return self.classical_head(q_outputs)


# ======================================================
# TRAINING
# ======================================================

def train_model(model, X_train_t, y_train_t, X_test_t, y_test_t, epochs=EPOCHS):

    # Keep the original dataset in RAM; move each batch to GPU.
    dataset = TensorDataset(X_train_t, y_train_t)

    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        pin_memory=True
    )

    class_weights = compute_class_weight(
        class_weight="balanced",
        classes=np.unique(y_train_t.numpy()),
        y=y_train_t.numpy()
    )

    class_weights = torch.tensor(
        class_weights,
        dtype=torch.float32,
        device=torch_device
    )

    model = model.to(torch_device)

    criterion = nn.CrossEntropyLoss(weight=class_weights)

    optimizer = optim.Adam(
        model.parameters(),
        lr=0.003
    )

    print(
        f"\nDataset: {DATASET} | "
        f"Entanglement: {ENTANGLEMENT} | "
        f"Epochs: {epochs}"
    )
    print("-" * 45)

    model.train()

    for epoch in range(epochs):

        total_loss = 0.0

        for xb, yb in loader:

            # GPU transfer
            xb = xb.to(torch_device, non_blocking=True)
            yb = yb.to(torch_device, non_blocking=True)

            optimizer.zero_grad(set_to_none=True)

            outputs = model(xb)
            loss = criterion(outputs, yb)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(
                f"Epoch {epoch + 1:>3}, "
                f"Loss: {total_loss:.4f}"
            )

    # ==================================================
    # EVALUATION
    # ==================================================

    model.eval()

    with torch.no_grad():

        train_preds = torch.argmax(
            model(X_train_t.to(torch_device)),
            dim=1
        ).cpu()

        test_preds = torch.argmax(
            model(X_test_t.to(torch_device)),
            dim=1
        ).cpu()

    train_acc = (train_preds == y_train_t).float().mean().item()
    test_acc = (test_preds == y_test_t).float().mean().item()

    print(f"\nTrain Accuracy : {train_acc:.4f}")
    print(f"Test  Accuracy : {test_acc:.4f}")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test_t.numpy(),
            test_preds.numpy(),
            target_names=[
                "Healthy(0)",
                "Degrading(1)",
                "Failure(2)"
            ],
            zero_division=0
        )
    )

    recalls = recall_score(
        y_test_t.numpy(),
        test_preds.numpy(),
        average=None,
        zero_division=0
    )

    return test_acc, recalls


# ======================================================
# SINGLE EXPERIMENT
# ======================================================

def run_experiment(dataset_name, entanglement_type, seed, features, labels):

    global ENTANGLEMENT, DATASET

    ENTANGLEMENT = entanglement_type
    DATASET = dataset_name

    print(f"\n{'=' * 50}")
    print(
        f"Dataset: {dataset_name} | "
        f"Topology: {entanglement_type.upper()} | "
        f"Seed: {seed}"
    )
    print("=" * 50)

    set_seed(seed)

    # Feature scaling
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Stratified train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        features_scaled,
        labels,
        test_size=0.2,
        random_state=seed,
        stratify=labels
    )

    # CPU tensors initially
    X_train_t = torch.tensor(X_train, dtype=torch.float32)
    X_test_t = torch.tensor(X_test, dtype=torch.float32)

    y_train_t = torch.tensor(y_train.values, dtype=torch.long)
    y_test_t = torch.tensor(y_test.values, dtype=torch.long)

    # Dataset-size cap
    rng = np.random.default_rng(seed)

    train_idx = rng.choice(
        len(X_train_t),
        size=min(7000, len(X_train_t)),
        replace=False
    )

    test_idx = rng.choice(
        len(X_test_t),
        size=min(1000, len(X_test_t)),
        replace=False
    )

    X_train_t = X_train_t[train_idx]
    y_train_t = y_train_t[train_idx]

    X_test_t = X_test_t[test_idx]
    y_test_t = y_test_t[test_idx]

    print(f"Train: {X_train_t.shape} | Test: {X_test_t.shape}")

    print(
        f"Train class dist: "
        f"{torch.bincount(y_train_t).tolist()}"
    )

    print(
        f"Test class dist: "
        f"{torch.bincount(y_test_t).tolist()}"
    )

    model = HybridModel(input_dim=X_train_t.shape[1])

    return train_model(
        model,
        X_train_t,
        y_train_t,
        X_test_t,
        y_test_t
    )


# ======================================================
# MULTI-SEED / MULTI-TOPOLOGY EXECUTION
# ======================================================

if __name__ == "__main__":

    datasets = ["FD001"]

    seeds = [7, 2024]

    topologies = ["ring", "full"]

    all_results = {}

    for dataset_name in datasets:

        features, labels = load_dataset(dataset_name)

        results = {
            topology: {
                "acc": [],
                "recall_0": [],
                "recall_1": [],
                "recall_2": []
            }
            for topology in topologies
        }

        for topology in topologies:

            for seed in seeds:

                accuracy, recalls = run_experiment(
                    dataset_name,
                    topology,
                    seed,
                    features,
                    labels
                )

                results[topology]["acc"].append(accuracy)
                results[topology]["recall_0"].append(recalls[0])
                results[topology]["recall_1"].append(recalls[1])
                results[topology]["recall_2"].append(recalls[2])

        all_results[dataset_name] = results

        print("\n" + "=" * 70)
        print(f"FINAL MULTI-SEED RESULTS — {dataset_name}")
        print("=" * 70)

        print(
            f"{'Topology':<10}"
            f"{'Accuracy':>15}"
            f"{'R-Healthy':>15}"
            f"{'R-Degrad':>15}"
            f"{'R-Failure':>15}"
        )

        print("-" * 70)

        for topology in topologies:

            r = results[topology]

            acc_mean = np.mean(r["acc"])
            acc_std = np.std(r["acc"])

            r0_mean = np.mean(r["recall_0"])
            r0_std = np.std(r["recall_0"])

            r1_mean = np.mean(r["recall_1"])
            r1_std = np.std(r["recall_1"])

            r2_mean = np.mean(r["recall_2"])
            r2_std = np.std(r["recall_2"])

            print(
                f"{topology:<10}"
                f"{acc_mean:.3f} ± {acc_std:.3f}  "
                f"{r0_mean:.3f} ± {r0_std:.3f}  "
                f"{r1_mean:.3f} ± {r1_std:.3f}  "
                f"{r2_mean:.3f} ± {r2_std:.3f}"
            )

        mean_accs = [
            np.mean(results[topology]["acc"])
            for topology in topologies
        ]

        topology_sensitivity = np.std(mean_accs)

        print(
            f"\nTopology Sensitivity for {dataset_name}: "
            f"{topology_sensitivity:.4f}"
        )
        print("=" * 70)
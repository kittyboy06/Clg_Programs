import torch
import torch.nn as nn
import torch.optim as optim
import pennylane as qml
import numpy as np
import pandas as pd
import os
import random

from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report, recall_score

# ======================================================
# SETTINGS
# ======================================================

n_qubits  = 6
n_layers  = 3
n_classes = 3
EPOCHS    = 35

ENTANGLEMENT = None     # Set dynamically per run
DATASET      = None     # Set dynamically per run ("FD002" or "FD003")

device = qml.device("lightning.qubit", wires=n_qubits)

# ======================================================
# SEED FUNCTION
# ======================================================

def set_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)

# ======================================================
# DATA LOADING (parameterized by dataset name)
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_dataset(dataset_name):
    """dataset_name: 'FD002' or 'FD003' (matches train_FD00X.txt filename)."""

    data_path = os.path.join(f"train_{dataset_name}.txt")
    print(f"Loading {dataset_name} dataset from {data_path} ...")

    df = pd.read_csv(data_path, sep=" ", header=None)
    df = df.dropna(axis=1)

    df['RUL'] = df.groupby(0)[1].transform('max') - df[1]

    def label_rul(rul):
        if rul > 80:
            return 0
        elif rul > 30:
            return 1
        else:
            return 2

    df['label'] = df['RUL'].apply(label_rul)

    feats  = df.drop(columns=[0, 1, 'RUL', 'label'])
    labs   = df['label']

    print(f"Total samples: {len(feats)}")
    print(f"Class distribution: {labs.value_counts().sort_index().to_dict()}\n")

    return feats, labs

# ======================================================
# FEATURE EXTRACTOR
# ======================================================

class FeatureExtractor(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 6)
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
# QUANTUM CIRCUIT
# ======================================================

@qml.qnode(device, interface="torch")
def quantum_circuit(inputs, weights):

    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)

    for l in range(n_layers):

        for i in range(n_qubits):
            qml.RX(weights[l, i, 0], wires=i)
            qml.RZ(weights[l, i, 1], wires=i)

        if ENTANGLEMENT == "linear":
            linear_entanglement()
        elif ENTANGLEMENT == "ring":
            ring_entanglement()
        elif ENTANGLEMENT == "full":
            full_entanglement()

        # Data re-upload
        for i in range(n_qubits):
            qml.RY(inputs[i], wires=i)

    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# ======================================================
# HYBRID MODEL
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

        latent = self.feature_extractor(x)
        latent = torch.tanh(latent)
        latent_scaled = (latent + 1) * (np.pi / 2)

        q_outputs = []
        for sample in latent_scaled:
            q_out = torch.stack(quantum_circuit(sample, self.q_params))
            q_outputs.append(q_out)

        q_outputs = torch.stack(q_outputs).float()

        return self.classical_head(q_outputs)

# ======================================================
# TRAINING FUNCTION
# ======================================================

def train_model(model, X_train_t, y_train_t, X_test_t, y_test_t, epochs=EPOCHS):

    dataset = TensorDataset(X_train_t, y_train_t)
    loader  = DataLoader(dataset, batch_size=32, shuffle=True)

    class_weights = compute_class_weight(
        class_weight="balanced",
        classes=np.unique(y_train_t.numpy()),
        y=y_train_t.numpy()
    )
    class_weights = torch.tensor(class_weights, dtype=torch.float32)

    criterion = nn.CrossEntropyLoss(weight=class_weights)
    optimizer = optim.Adam(model.parameters(), lr=0.003)

    print(f"\nDataset: {DATASET} | Entanglement: {ENTANGLEMENT} | Epochs: {epochs}")
    print("-" * 45)

    for epoch in range(epochs):
        total_loss = 0
        for xb, yb in loader:
            optimizer.zero_grad()
            outputs = model(xb)
            loss    = criterion(outputs, yb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"Epoch {epoch+1:>3}, Loss: {total_loss:.4f}")

    # ── Evaluation ──────────────────────────────────────
    with torch.no_grad():
        train_preds = torch.argmax(model(X_train_t), dim=1)
        test_preds  = torch.argmax(model(X_test_t),  dim=1)

        train_acc = (train_preds == y_train_t).float().mean().item()
        test_acc  = (test_preds  == y_test_t).float().mean().item()

    print(f"\nTrain Accuracy : {train_acc:.4f}")
    print(f"Test  Accuracy : {test_acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(
        y_test_t.numpy(),
        test_preds.numpy(),
        target_names=["Healthy(0)", "Degrading(1)", "Failure(2)"]
    ))

    recalls = recall_score(
        y_test_t.numpy(),
        test_preds.numpy(),
        average=None
    )

    return test_acc, recalls

# ======================================================
# SINGLE EXPERIMENT
# ======================================================

def run_experiment(dataset_name, entanglement_type, seed, features, labels):

    global ENTANGLEMENT, DATASET
    ENTANGLEMENT = entanglement_type
    DATASET      = dataset_name

    print(f"\n{'='*50}")
    print(f"  Dataset: {dataset_name}  |  Topology: {entanglement_type.upper()}  |  Seed: {seed}")
    print(f"{'='*50}")

    set_seed(seed)

    # Scale features
    scaler          = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Stratified split — preserves class balance
    X_train, X_test, y_train, y_test = train_test_split(
        features_scaled,
        labels,
        test_size=0.2,
        random_state=seed,
        stratify=labels
    )

    X_train_t = torch.tensor(X_train, dtype=torch.float32)
    X_test_t  = torch.tensor(X_test,  dtype=torch.float32)
    y_train_t = torch.tensor(y_train.values, dtype=torch.long)
    y_test_t  = torch.tensor(y_test.values,  dtype=torch.long)

    # Random subsetting (same cap as FD001 run — adjust if FD002/FD003 need different sizes)
    rng           = np.random.default_rng(seed)
    train_idx     = rng.choice(len(X_train_t), size=min(7000, len(X_train_t)), replace=False)
    test_idx      = rng.choice(len(X_test_t),  size=min(1000, len(X_test_t)),  replace=False)

    X_train_t = X_train_t[train_idx]
    y_train_t = y_train_t[train_idx]
    X_test_t  = X_test_t[test_idx]
    y_test_t  = y_test_t[test_idx]

    print(f"Train: {X_train_t.shape} | Test: {X_test_t.shape}")
    print(f"Train class dist: {torch.bincount(y_train_t).tolist()}")
    print(f"Test  class dist: {torch.bincount(y_test_t).tolist()}")

    model = HybridModel(input_dim=X_train_t.shape[1])

    test_acc, recalls = train_model(
        model, X_train_t, y_train_t, X_test_t, y_test_t
    )

    return test_acc, recalls

# ======================================================
# MULTI-SEED / MULTI-DATASET EXECUTION
# ======================================================

if __name__ == "__main__":

    datasets   = ["FD001"]
    seeds      = [7, 2024]   # 5 seeds
    topologies = ["ring","full"]

    all_results = {}  # all_results[dataset][topology] = {"acc": [...], "recall_0": [...], ...}

    for dataset_name in datasets:

        features, labels = load_dataset(dataset_name)

        results = {
            t: {"acc": [], "recall_0": [], "recall_1": [], "recall_2": []}
            for t in topologies
        }

        for topology in topologies:
            for seed in seeds:
                acc, recalls = run_experiment(dataset_name, topology, seed, features, labels)
                results[topology]["acc"].append(acc)
                results[topology]["recall_0"].append(recalls[0])
                results[topology]["recall_1"].append(recalls[1])
                results[topology]["recall_2"].append(recalls[2])

        all_results[dataset_name] = results

        # ── Per-dataset summary ──────────────────────────
        print("\n" + "="*60)
        print(f"  FINAL MULTI-SEED RESULTS — {dataset_name}")
        print("="*60)
        print(f"{'Topology':<10} {'Accuracy':>12} {'R-Healthy':>12} {'R-Degrad':>12} {'R-Failure':>12}")
        print("-"*60)

        for topology in topologies:
            r      = results[topology]
            acc_m  = np.mean(r["acc"]);      acc_s  = np.std(r["acc"])
            r0_m   = np.mean(r["recall_0"]); r0_s   = np.std(r["recall_0"])
            r1_m   = np.mean(r["recall_1"]); r1_s   = np.std(r["recall_1"])
            r2_m   = np.mean(r["recall_2"]); r2_s   = np.std(r["recall_2"])

            print(f"{topology:<10} "
                  f"{acc_m:.3f}±{acc_s:.3f}  "
                  f"{r0_m:.3f}±{r0_s:.3f}  "
                  f"{r1_m:.3f}±{r1_s:.3f}  "
                  f"{r2_m:.3f}±{r2_s:.3f}")

        print("="*60)
        print("\nRaw accuracy results:")
        for topology in topologies:
            print(f"  {topology}: {[round(x,4) for x in results[topology]['acc']]}")

        # ── Topology Sensitivity Metric (per dataset) ────
        mean_accs = [np.mean(results[t]["acc"]) for t in topologies]
        topo_sensitivity = np.std(mean_accs)
        print(f"\nTopology Sensitivity for {dataset_name} (std of mean accuracies): {topo_sensitivity:.4f}")

    # ── Cross-dataset comparison ─────────────────────────
    print("\n" + "="*60)
    print("  CROSS-DATASET TOPOLOGY SENSITIVITY SUMMARY")
    print("="*60)
    for dataset_name in datasets:
        mean_accs = [np.mean(all_results[dataset_name][t]["acc"]) for t in topologies]
        topo_sensitivity = np.std(mean_accs)
        print(f"  {dataset_name}: {topo_sensitivity:.4f}  "
              f"(compare against FD001's value from your prior run)")
    print("="*60)
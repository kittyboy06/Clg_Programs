# Program 11: k-Nearest Neighbors (k-NN) Classifier on Iris Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load dataset
df = pd.read_csv('datasets/iris.csv')
X = df.drop(columns=['species'])
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train k-NN model (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 3. Predict on test set
y_pred = knn.predict(X_test)
y_actual = y_test.values

# 4. Print both correct and wrong predictions
print("=== Prediction Analysis ===")
correct, wrong = [], []
for i in range(len(y_actual)):
    msg = f"Sample {i+1}: Actual='{y_actual[i]}', Predicted='{y_pred[i]}'"
    if y_actual[i] == y_pred[i]:
        correct.append(msg)
    else:
        wrong.append(msg)

print(f"\nCorrect Predictions ({len(correct)}):")
for item in correct[:5]:
    print(" ", item)
if len(correct) > 5:
    print(f"  ... and {len(correct) - 5} more correct predictions.")

print(f"\nWrong Predictions ({len(wrong)}):")
if wrong:
    for item in wrong:
        print(" ", item)
else:
    print("  None (100% accuracy on test set!)")

# 5. Accuracy and Confusion Matrix
acc = accuracy_score(y_actual, y_pred)
labels = sorted(y.unique())
cm = confusion_matrix(y_actual, y_pred, labels=labels)
print(f"\nk-NN Accuracy: {acc * 100:.2f}%")
print("Confusion Matrix:\n", cm)

# 6. Visualize Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=labels, yticklabels=labels)
plt.title(f'Confusion Matrix - k-NN (k=3, Acc: {acc*100:.1f}%)')
plt.xlabel('Predicted Species')
plt.ylabel('Actual Species')
plt.tight_layout()
plt.savefig('outputs/11_knn_classifier.png')
print("\nPlot saved as outputs/11_knn_classifier.png")
plt.show()

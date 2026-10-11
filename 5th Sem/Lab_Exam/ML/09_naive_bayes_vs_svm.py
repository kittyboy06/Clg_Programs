# Program 09: Compare Naive Bayes and Support Vector Machine (SVM) on Iris Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load dataset
df = pd.read_csv('datasets/iris.csv')
X = df.drop(columns=['species'])
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train and evaluate Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)
nb_acc = accuracy_score(y_test, nb_pred)

# 3. Train and evaluate SVM
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
svm_pred = svm_model.predict(X_test)
svm_acc = accuracy_score(y_test, svm_pred)

# 4. Print comparison
print("=== Performance Comparison ===")
print(f"Naive Bayes Accuracy: {nb_acc * 100:.2f}%")
print(f"SVM Accuracy:         {svm_acc * 100:.2f}%")

# 5. Visualize Confusion Matrices side-by-side
labels = sorted(y.unique())
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

sns.heatmap(confusion_matrix(y_test, nb_pred, labels=labels), annot=True, fmt='d', cmap='Greens',
            xticklabels=labels, yticklabels=labels, ax=axes[0])
axes[0].set_title(f'Naive Bayes (Acc: {nb_acc*100:.1f}%)')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')

sns.heatmap(confusion_matrix(y_test, svm_pred, labels=labels), annot=True, fmt='d', cmap='Blues',
            xticklabels=labels, yticklabels=labels, ax=axes[1])
axes[1].set_title(f'SVM (Acc: {svm_acc*100:.1f}%)')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')

plt.tight_layout()
plt.savefig('outputs/09_naive_bayes_vs_svm_comparison.png')
print("\nPlot saved as outputs/09_naive_bayes_vs_svm_comparison.png")
plt.show()

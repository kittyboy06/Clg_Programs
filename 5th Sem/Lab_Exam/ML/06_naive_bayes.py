# Program 06: Naive Bayes Classifier for Iris Species Identification
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load dataset
df = pd.read_csv('datasets/iris.csv')
X = df.drop(columns=['species'])
y = df['species']

# 2. Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# 4. Predict and compute accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
labels = sorted(y.unique())
cm = confusion_matrix(y_test, y_pred, labels=labels)

print(f"Naive Bayes Accuracy: {acc * 100:.2f}%")
print("Confusion Matrix:\n", cm)

# 5. Visualize performance evaluation (Confusion Matrix Heatmap)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix - Naive Bayes')
plt.xlabel('Predicted Species')
plt.ylabel('Actual Species')
plt.tight_layout()
plt.savefig('outputs/06_naive_bayes.png')
print("Plot saved as outputs/06_naive_bayes.png")
plt.show()

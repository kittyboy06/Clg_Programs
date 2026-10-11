# Program 05: Logistic Regression for Diabetes Diagnosis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load dataset
df = pd.read_csv('datasets/diabetes.csv')
X = df.drop(columns=['Outcome'])
y = df['Outcome']

# 2. Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 4. Predict and compute accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Logistic Regression Accuracy: {acc * 100:.2f}%")
print("Confusion Matrix:\n", cm)

# 5. Visualize performance evaluation (Confusion Matrix Heatmap)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.title('Confusion Matrix - Logistic Regression')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.tight_layout()
plt.savefig('outputs/05_logistic_regression.png')
print("Plot saved as outputs/05_logistic_regression.png")
plt.show()

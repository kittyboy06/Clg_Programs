# Program 10: Compare Logistic Regression and Naive Bayes on Diabetes Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load dataset
df = pd.read_csv('datasets/diabetes.csv')
X = df.drop(columns=['Outcome'])
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train and evaluate Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)

# 3. Train and evaluate Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)
nb_acc = accuracy_score(y_test, nb_pred)

# 4. Print comparison
print("=== Performance Comparison ===")
print(f"Logistic Regression Accuracy: {lr_acc * 100:.2f}%")
print(f"Naive Bayes Accuracy:         {nb_acc * 100:.2f}%")

# 5. Visualize Confusion Matrices side-by-side
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
labels = ['Negative', 'Positive']

sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, fmt='d', cmap='Blues',
            xticklabels=labels, yticklabels=labels, ax=axes[0])
axes[0].set_title(f'Logistic Regression (Acc: {lr_acc*100:.1f}%)')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')

sns.heatmap(confusion_matrix(y_test, nb_pred), annot=True, fmt='d', cmap='Greens',
            xticklabels=labels, yticklabels=labels, ax=axes[1])
axes[1].set_title(f'Naive Bayes (Acc: {nb_acc*100:.1f}%)')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')

plt.tight_layout()
plt.savefig('outputs/10_logistic_vs_naive_bayes_comparison.png')
print("\nPlot saved as outputs/10_logistic_vs_naive_bayes_comparison.png")
plt.show()

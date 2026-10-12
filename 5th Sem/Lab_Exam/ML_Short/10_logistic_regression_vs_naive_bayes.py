import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/diabetes.csv')
X, y = df.drop(columns=['Outcome']), df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_pred = LogisticRegression(max_iter=1000).fit(X_train, y_train).predict(X_test)
nb_pred = GaussianNB().fit(X_train, y_train).predict(X_test)

print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_pred) * 100:.2f}%")
print(f"Naive Bayes Accuracy:         {accuracy_score(y_test, nb_pred) * 100:.2f}%")

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, fmt='d', cmap='Blues', ax=axes[0])
sns.heatmap(confusion_matrix(y_test, nb_pred), annot=True, fmt='d', cmap='Greens', ax=axes[1])
axes[0].set_title('Logistic Regression')
axes[1].set_title('Naive Bayes')
plt.tight_layout()
plt.show()

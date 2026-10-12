import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/iris.csv')
X, y = df.drop(columns=['species']), df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_pred = GaussianNB().fit(X_train, y_train).predict(X_test)
svm_pred = SVC(kernel='linear').fit(X_train, y_train).predict(X_test)

print(f"Naive Bayes Accuracy: {accuracy_score(y_test, nb_pred) * 100:.2f}%")
print(f"SVM Accuracy:         {accuracy_score(y_test, svm_pred) * 100:.2f}%")

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.heatmap(confusion_matrix(y_test, nb_pred), annot=True, fmt='d', cmap='Greens', ax=axes[0])
sns.heatmap(confusion_matrix(y_test, svm_pred), annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[0].set_title('Naive Bayes')
axes[1].set_title('SVM')
plt.tight_layout()
plt.show()

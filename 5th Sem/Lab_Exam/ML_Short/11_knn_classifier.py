import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/iris.csv')
X, y = df.drop(columns=['species']), df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print correct and wrong predictions
print("Correct Predictions (first 5):", [(a, p) for a, p in zip(y_test, y_pred) if a == p][:5])
print("Wrong Predictions:", [(a, p) for a, p in zip(y_test, y_pred) if a != p])

print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=model.classes_, yticklabels=model.classes_)
plt.title('k-NN Confusion Matrix (k=3)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

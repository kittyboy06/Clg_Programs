import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

k = 5

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Correct Predictions:")
for actual, predicted in zip(y_test, y_pred):
    if actual == predicted:
        print("Actual:", iris.target_names[actual],
              "Predicted:", iris.target_names[predicted])

print("\nWrong Predictions:")
for actual, predicted in zip(y_test, y_pred):
    if actual != predicted:
        print("Actual:", iris.target_names[actual],
              "Predicted:", iris.target_names[predicted])
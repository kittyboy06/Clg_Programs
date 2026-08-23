import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("5.csv")

data = pd.get_dummies(data, drop_first=True)
data = data.dropna()

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Predicted Values:", predictions)
print("Actual Values:", y_test.values)
print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

train = pd.read_csv("5.csv")

X = train.iloc[:, :-1]
y = train.iloc[:, -1]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

for file in ["5_test1.csv", "5_test2.csv"]:
    test = pd.read_csv(file)

    X1 = test.iloc[:, :-1]
    y1 = test.iloc[:, -1]

    predictions = model.predict(X1)
    accuracy = accuracy_score(y1, predictions)

    print("\n", file)
    print("Predicted Values:", predictions)
    print("Accuracy:", accuracy)
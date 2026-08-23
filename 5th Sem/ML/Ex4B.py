import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

train = pd.read_csv("train_data.csv")

X = train.iloc[:, :-1]
y = train.iloc[:, -1]

model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)

model.fit(X, y)

print("Model Coefficients:", model[-1].coef_)
print("Intercept:", model[-1].intercept_)

for file in ["test_data1.csv", "test_data2.csv"]:
    test = pd.read_csv(file)

    X1 = test.iloc[:, :-1]
    y1 = test.iloc[:, -1]

    predictions = model.predict(X1)
    mse = mean_squared_error(y1, predictions)

    print("\n", file)
    print("Predicted Values:", predictions)
    print("MSE:", mse)
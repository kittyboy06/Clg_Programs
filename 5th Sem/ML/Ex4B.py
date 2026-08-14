import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

train_data = pd.read_csv("train_data.csv")

X = train_data.iloc[:, :-1]
Y = train_data.iloc[:, -1]

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)

print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

test_files = ["test_data1.csv", "test_data2.csv", "test_data3.csv"]

for file in test_files:
    print("\n====================================")
    print("Testing on:", file)

    test_data = pd.read_csv(file)

    X1 = test_data.iloc[:, :-1]
    Y1 = test_data.iloc[:, -1]

    X1_poly = poly.transform(X1)

    Y_pred = model.predict(X1_poly)

    mse = mean_squared_error(Y1, Y_pred)

    print("Predicted Values:")
    print(Y_pred)

    print("Mean Squared Error (MSE):", mse)
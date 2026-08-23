import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = pd.read_csv("heart.csv")

data = pd.get_dummies(data, drop_first=True)
data = data.dropna()

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

nonlinear_model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)
nonlinear_model.fit(X_train, y_train)

linear_pred = linear_model.predict(X_test)
nonlinear_pred = nonlinear_model.predict(X_test)

def evaluate(y, pred):
    mse = mean_squared_error(y, pred) 
    rmse = mse ** 0.5
    mae = mean_absolute_error(y, pred)
    r2 = r2_score(y, pred)
    return mse, rmse, mae, r2

linear = evaluate(y_test, linear_pred)
nonlinear = evaluate(y_test, nonlinear_pred)

print("Linear Regression")
print("MSE:", linear[0])
print("RMSE:", linear[1])
print("MAE:", linear[2])
print("R2 Score:", linear[3])

print("\nNon-Linear Regression")
print("MSE:", nonlinear[0])
print("RMSE:", nonlinear[1])
print("MAE:", nonlinear[2])
print("R2 Score:", nonlinear[3])

print("\nBetter Model:",
      "Linear Regression" if linear[0] < nonlinear[0] else "Non-Linear Regression")

plt.scatter(y_test, linear_pred, label="Linear Regression")
plt.scatter(y_test, nonlinear_pred, label="Non-Linear Regression")
plt.xlabel("Actual Diagnosis")
plt.ylabel("Predicted Diagnosis")
plt.legend()
plt.show()
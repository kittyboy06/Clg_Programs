import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = pd.read_csv("heart.csv")

X = data.drop("target", axis=1)
y = data["target"]

X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)

y_pred_linear = linear_model.predict(X_test_scaled)

poly_model = Pipeline([
    ("poly", PolynomialFeatures(degree=2)),
    ("linear", LinearRegression())
])

poly_model.fit(X_train_scaled, y_train)

y_pred_poly = poly_model.predict(X_test_scaled)

def evaluate(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    return mse, rmse, mae, r2

linear_metrics = evaluate(y_test, y_pred_linear)
poly_metrics = evaluate(y_test, y_pred_poly)

print("===== Linear Regression =====")
print("MSE :", linear_metrics[0])
print("RMSE:", linear_metrics[1])
print("MAE :", linear_metrics[2])
print("R2 Score:", linear_metrics[3])

print("\n===== Polynomial Regression =====")
print("MSE :", poly_metrics[0])
print("RMSE:", poly_metrics[1])
print("MAE :", poly_metrics[2])
print("R2 Score:", poly_metrics[3])

# Compare models
print("\n===== Model Comparison =====")
if poly_metrics[0] < linear_metrics[0]:
    print("Polynomial Regression performs better.")
else:
    print("Linear Regression performs better.")

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred_linear, color="blue", label="Linear Regression")
plt.scatter(y_test, y_pred_poly, color="red", label="Polynomial Regression")

plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="black",
         linestyle="--")

plt.xlabel("Actual Target")
plt.ylabel("Predicted Target")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.show()
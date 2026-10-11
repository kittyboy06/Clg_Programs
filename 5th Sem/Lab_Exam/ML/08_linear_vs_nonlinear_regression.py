# Program 08: Compare Linear and Non-linear Regression for House Price Prediction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv('datasets/house_prices.csv')
X = df[['SquareFeet']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

# 3. Non-linear Regression Model (Polynomial Degree 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

nonlinear_model = LinearRegression()
nonlinear_model.fit(X_train_poly, y_train)
y_pred_poly = nonlinear_model.predict(X_test_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

# 4. Compare performance
print("=== Performance Comparison ===")
print(f"Linear Regression:     MSE = {mse_linear:.2f}, R2 = {r2_linear:.4f}")
print(f"Non-linear Regression: MSE = {mse_poly:.2f}, R2 = {r2_poly:.4f}")

# 5. Visualize comparison
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='gray', label='Actual Test Data', alpha=0.7)

# Plot Linear fit
plt.plot(X_test, y_pred_linear, color='blue', linewidth=2, label='Linear Regression')

# Plot Non-linear fit (sorted for smooth curve)
sort_idx = np.argsort(X_test.values.flatten())
plt.plot(X_test.values[sort_idx], y_pred_poly[sort_idx], color='red', linewidth=2, label='Non-linear (Polynomial)')

plt.title('Comparison: Linear vs Non-linear Regression')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/08_linear_vs_nonlinear_comparison.png')
print("\nPlot saved as outputs/08_linear_vs_nonlinear_comparison.png")
plt.show()

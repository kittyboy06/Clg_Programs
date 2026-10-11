# Program 04: Non-linear Regression (Polynomial Regression) for House Price Prediction
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

# 2. Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Transform features for Non-linear (Polynomial) Regression (Degree 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# 4. Train model and predict
model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Non-linear (Polynomial) Regression Results:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R2): {r2:.4f}")

# 5. Visualize performance evaluation
plt.figure(figsize=(7, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')

# Sort values to plot a smooth non-linear curve
sort_idx = np.argsort(X_test.values.flatten())
plt.plot(X_test.values[sort_idx], y_pred[sort_idx], color='red', linewidth=2, label='Polynomial Fit (Degree 2)')

plt.title('House Price Prediction - Non-linear Regression')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/04_nonlinear_regression.png')
print("Plot saved as outputs/04_nonlinear_regression.png")
plt.show()

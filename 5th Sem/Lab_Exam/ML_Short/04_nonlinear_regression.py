import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('datasets/house_prices.csv')
X, y = df[['SquareFeet']], df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

poly = PolynomialFeatures(degree=2)
model = LinearRegression().fit(poly.fit_transform(X_train), y_train)
y_pred = model.predict(poly.transform(X_test))

print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))

# Sort test inputs to display smooth non-linear curve
idx = np.argsort(X_test.values.flatten())
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test.values[idx], y_pred[idx], color='red', label='Polynomial Fit')
plt.title('Non-linear Regression - House Prices')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.show()

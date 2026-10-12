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

# 1. Linear Regression
lr = LinearRegression().fit(X_train, y_train)
y_lr = lr.predict(X_test)

# 2. Non-linear (Polynomial) Regression
poly = PolynomialFeatures(degree=2)
nlr = LinearRegression().fit(poly.fit_transform(X_train), y_train)
y_nlr = nlr.predict(poly.transform(X_test))

print("Linear Regression MSE:", mean_squared_error(y_test, y_lr))
print("Non-linear Regression MSE:", mean_squared_error(y_test, y_nlr))

# 3. Visualization
idx = np.argsort(X_test.values.flatten())
plt.scatter(X_test, y_test, color='gray', label='Actual Data')
plt.plot(X_test, y_lr, color='blue', label='Linear')
plt.plot(X_test.values[idx], y_nlr[idx], color='red', label='Non-linear (Degree 2)')
plt.title('Linear vs Non-linear Regression')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.show()

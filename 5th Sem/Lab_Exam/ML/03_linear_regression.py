# Program 03: Linear Regression for House Price Prediction
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv('datasets/house_prices.csv')
X = df[['SquareFeet']]  # Feature
y = df['Price']         # Target

# 2. Split dataset into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict on test set and compute Mean Squared Error (MSE)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression Results:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R2): {r2:.4f}")

# 5. Visualize performance evaluation
plt.figure(figsize=(7, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('House Price Prediction - Linear Regression')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/03_linear_regression.png')
print("Plot saved as outputs/03_linear_regression.png")
plt.show()

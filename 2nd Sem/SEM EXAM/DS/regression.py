import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("D:\\Clg\\Clg_Programs\\2nd Sem\\SEM EXAM\\DS\\iris.csv",header=0)
cn = list(data.columns)
print("Available columns:", cn)
x = input("Enter the first column name for Linear Regression:")
y = input("Enter the second column name for Linear Regression:")
X, Y = data[[x]], data[[y]]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
print("Coefficients:", model.coef_)
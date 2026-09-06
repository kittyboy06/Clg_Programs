import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data.csv")

print("Dataset:")
print(df.head())

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

series = df["Value"].dropna()

plt.figure(figsize=(10, 5))
plt.plot(series)
plt.title("Original Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.show()

log_series = np.log(series)

df = pd.DataFrame({"Value": series, "LogValue": log_series})
df["Time"] = np.arange(len(df))

df["Differenced"] = df["LogValue"].diff()

df["MovingAverage"] = df["Value"].rolling(window=3).mean()

X = df[["Time"]]
y = df["LogValue"]

model = LinearRegression()
model.fit(X, y)

predicted_log = model.predict(X)
predicted = np.exp(predicted_log)

mae = mean_absolute_error(df["Value"], predicted)
rmse = np.sqrt(mean_squared_error(df["Value"], predicted))

print("\nModel Coefficient:", model.coef_[0])
print("Model Intercept:", model.intercept_)

print("\nMean Absolute Error (MAE):", round(mae, 4))
print("Root Mean Squared Error (RMSE):", round(rmse, 4))

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Value"], label="Actual")
plt.plot(df.index, predicted, label="Predicted")
plt.title("Actual vs Predicted Values")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

residuals = df["Value"] - predicted

plt.figure(figsize=(10, 5))
plt.plot(df.index, residuals)
plt.axhline(0, linestyle="--")
plt.title("Residual Analysis")
plt.xlabel("Time")
plt.ylabel("Residual")
plt.grid(True)
plt.show()

print("\nPredicted Values:")
print(predicted)

print("\nProgram completed successfully.")
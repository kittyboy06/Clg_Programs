import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv("data.csv")

print("Dataset:")
print(df.head())

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

series = df["Value"].dropna()

plt.figure(figsize=(10, 5))
plt.plot(series, label="Original Series")
plt.title("Original Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

model = SimpleExpSmoothing(series)

fit = model.fit(optimized=True)

alpha = fit.params["smoothing_level"]

smoothed_values = fit.fittedvalues

print("\nOptimized Alpha:", round(alpha, 4))

plt.figure(figsize=(10, 5))
plt.plot(series, label="Original Series")
plt.plot(smoothed_values, label="Smoothed Series")
plt.title("First-Order Exponential Smoothing")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

mae = mean_absolute_error(series, smoothed_values)
rmse = np.sqrt(mean_squared_error(series, smoothed_values))

print("\nForecast Performance:")
print("MAE :", round(mae, 4))
print("RMSE:", round(rmse, 4))

print("\nProgram completed successfully.")
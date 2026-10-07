import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["date"])

# Set date as index
df.set_index("Date", inplace=True)

# Sort by date
df.sort_index(inplace=True)

# Select time series
series = df["Value"].dropna()

# Set monthly frequency
series = series.asfreq("MS")

# Plot original series
plt.plot(series)
plt.title("Original Time Series")
plt.show()

# ADF Test
result = adfuller(series.dropna(), maxlag=1, regression="c", autolag=None)

print("ADF p-value:", round(result[1], 4))

# Determine differencing
d = 1 if result[1] > 0.05 else 0

# SARIMA parameters
p, q = 1, 1
P, Q = 0, 0
D = 0
s = 12

# Train-test split
n = int(len(series) * 0.8)

train = series.iloc[:n]
test = series.iloc[n:]

# SARIMA model
model = SARIMAX(
    train,
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)

# Fit model
fit = model.fit(disp=False)

# Forecast test period
forecast = fit.forecast(steps=len(test))

# Evaluation
mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("SARIMA Parameters:", (p, d, q, P, D, Q, s))
print("MAE:", round(mae, 4))
print("RMSE:", round(rmse, 4))

# Plot actual vs forecast
plt.figure(figsize=(10, 5))
plt.plot(series, label="Actual")
plt.plot(test.index, forecast, label="Forecast")
plt.title("Actual vs Forecast")
plt.legend()
plt.show()

# Future forecast
future = fit.forecast(steps=12)

print("\nFuture Forecast:")
print(future)

# Plot future forecast
plt.figure(figsize=(10, 5))
plt.plot(series, label="Actual")
plt.plot(future.index, future, label="Future Forecast")
plt.title("Future Forecast")
plt.legend()
plt.show()
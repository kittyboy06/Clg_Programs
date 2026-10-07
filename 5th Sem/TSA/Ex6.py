import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Read dataset
df = pd.read_csv("data.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Set date as index
df.set_index("Date", inplace=True)

# Sort by date
df.sort_index(inplace=True)

# Select value column
series = df["Value"].dropna()

# Plot original series
plt.figure(figsize=(10, 5))
plt.plot(series.index, series.values, marker="o")
plt.title("Original Time Series")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.show()


# -----------------------------
# ADF TEST
# -----------------------------

result = adfuller(
    series,
    maxlag=1,
    regression="c",
    autolag=None
)

print("ADF p-value:", round(result[1], 4))

# Differencing
d = 1 if result[1] > 0.05 else 0


# -----------------------------
# SARIMA PARAMETERS
# -----------------------------

p, q = 1, 1
P, Q = 0, 0
D = 0
s = 12


# -----------------------------
# TRAIN / TEST SPLIT
# -----------------------------

n = int(len(series) * 0.8)

train = series.iloc[:n]
test = series.iloc[n:]

print("\nTraining samples:", len(train))
print("Testing samples:", len(test))


# -----------------------------
# SARIMA MODEL
# -----------------------------

model = SARIMAX(
    train,
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)

fit = model.fit(disp=False)


# -----------------------------
# TEST FORECAST
# -----------------------------

forecast = fit.forecast(steps=len(test))

# Give forecast the same index as test
forecast.index = test.index


# -----------------------------
# EVALUATION
# -----------------------------

mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("\nSARIMA Parameters:", (p, d, q, P, D, Q, s))
print("MAE:", round(mae, 4))
print("RMSE:", round(rmse, 4))


# -----------------------------
# ACTUAL VS FORECAST
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    series.index,
    series.values,
    label="Actual",
    marker="o"
)

plt.plot(
    test.index,
    forecast.values,
    label="Forecast",
    marker="o"
)

plt.title("Actual vs Forecast")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()


# -----------------------------
# FUTURE FORECAST
# -----------------------------

future = fit.forecast(steps=12)

# Create future monthly dates
future_dates = pd.date_range(
    start=series.index[-1] + pd.DateOffset(months=1),
    periods=12,
    freq="MS"
)

future.index = future_dates

print("\nFuture Forecast:")
print(future)


# -----------------------------
# FUTURE FORECAST GRAPH
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    series.index,
    series.values,
    label="Actual",
    marker="o"
)

plt.plot(
    future.index,
    future.values,
    label="Future Forecast",
    marker="o"
)

plt.title("Future Forecast")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
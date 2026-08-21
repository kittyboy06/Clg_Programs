import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.read_csv("seasonal_sales.csv", parse_dates=["Date"])
data.set_index("Date", inplace=True)
data = data.asfreq("MS")

print("Dataset loaded successfully.")
print("Total observations:", len(data))

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Sales"], marker="o")
plt.title("Monthly Sales Data")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

result = adfuller(data["Sales"])
print("\nADF Test")
print("ADF Statistic:", round(result[0], 4))
print("p-value:", round(result[1], 4))

if result[1] < 0.05:
    print("Result: Stationary")
else:
    print("Result: Non-stationary")

p, d, q = 1, 1, 1
P, D, Q, s = 1, 1, 1, 12

print("\nSARIMA Parameters")
print("Order:", (p, d, q))
print("Seasonal Order:", (P, D, Q, s))

train_size = int(len(data) * 0.80)
train = data.iloc[:train_size]
test = data.iloc[train_size:]

print("\nData Split")
print("Training observations:", len(train))
print("Testing observations:", len(test))

model = SARIMAX(
    train["Sales"],
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)
model_fit = model.fit(disp=False)

forecast = model_fit.get_forecast(steps=len(test))
forecast_values = forecast.predicted_mean

plt.figure(figsize=(10, 5))
plt.plot(train.index, train["Sales"], label="Training Data")
plt.plot(test.index, test["Sales"], label="Actual")
plt.plot(test.index, forecast_values, label="Forecast")
plt.title("SARIMA Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

actual = test["Sales"]
mae = mean_absolute_error(actual, forecast_values)
rmse = np.sqrt(mean_squared_error(actual, forecast_values))
mape = np.mean(np.abs((actual - forecast_values) / actual)) * 100

print("\nForecast Accuracy")
print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("MAPE:", round(mape, 2), "%")

future_steps = 12

future_model = SARIMAX(
    data["Sales"],
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)
future_model_fit = future_model.fit(disp=False)
future_forecast = future_model_fit.get_forecast(steps=future_steps)
future_values = future_forecast.predicted_mean

print("\nFuture 12-Month Forecast")
for date, value in future_values.items():
    print(date.strftime("%Y-%m"), ":", round(value, 2))

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Sales"], label="Historical Data")
plt.plot(future_values.index, future_values, label="Future Forecast", marker="o")
plt.title("Future 12-Month SARIMA Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

print("\nSARIMA Modeling Completed Successfully.")
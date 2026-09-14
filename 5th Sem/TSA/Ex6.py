import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["date"])
df.set_index("Date", inplace=True)

series = df["Value"].dropna()

plt.plot(series)
plt.title("Original Time Series")
plt.show()

result = adfuller(series, maxlag=1, regression="c", autolag=None)
print("ADF p-value:", round(result[1], 4))

d = 1 if result[1] > 0.05 else 0

p, q = 1, 1
P, Q = 0, 0
D = 0
s = 12

n = int(len(series) * 0.8)

train = series[:n]
test = series[n:]

model = SARIMAX(
    train,
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False
)

fit = model.fit(disp=False)

forecast = fit.forecast(len(test))

mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("SARIMA Parameters:", (p, d, q, P, D, Q, s))
print("MAE:", round(mae, 4))
print("RMSE:", round(rmse, 4))

plt.plot(series, label="Actual")
plt.plot(test.index, forecast, label="Forecast")
plt.title("Actual vs Forecast")
plt.legend()
plt.show()

future = fit.forecast(steps=12)

print("Future Forecast:")
print(future)

plt.plot(series, label="Actual")
plt.plot(future.index, future, label="Future Forecast")
plt.title("Future Forecast")
plt.legend()
plt.show()
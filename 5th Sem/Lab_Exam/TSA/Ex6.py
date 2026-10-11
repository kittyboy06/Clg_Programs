import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
series = df["Value"]

plt.figure()
plt.plot(series)
plt.title("Original Series")
plt.show()

print("ADF p-value:", adfuller(series)[1])

p, d, q = 1, 1, 1
P, D, Q, s = 0, 0, 0, 12

n = int(len(series) * 0.8)
train = series[:n]
test = series[n:]

model = SARIMAX(train, order=(p, d, q), seasonal_order=(P, D, Q, s))
fit = model.fit(disp=False)

pred = fit.forecast(steps=len(test))

print("MAE:", mean_absolute_error(test, pred))
print("RMSE:", np.sqrt(mean_squared_error(test, pred)))

plt.figure()
plt.plot(series.index, series, label="Actual")
plt.plot(test.index, pred, label="Forecast")
plt.title("Actual vs Forecast")
plt.legend()
plt.show()

future = fit.forecast(steps=12)
plt.figure()
plt.plot(future)
plt.title("Future Forecast")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
series = df["Value"]

plt.figure()
plt.plot(series)
plt.title("Original Time Series")
plt.show()

print("ADF p-value:", adfuller(series)[1])

diff_series = series.diff().dropna()
d = 1

plot_acf(diff_series, lags=10)
plt.show()

plot_pacf(diff_series, lags=10)
plt.show()

p, q = 1, 1

train = series[:-5]
test = series[-5:]

model = ARIMA(train, order=(p, d, q))
fit = model.fit()

pred = fit.forecast(steps=len(test))

print("MAE:", mean_absolute_error(test, pred))
print("RMSE:", np.sqrt(mean_squared_error(test, pred)))

plt.figure()
plt.plot(test.index, test, label="Actual")
plt.plot(test.index, pred, label="Predicted")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()

print("Future Forecast:")
print(fit.forecast(steps=5))

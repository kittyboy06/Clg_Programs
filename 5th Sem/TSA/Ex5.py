import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data.csv")

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

series = df["Value"].dropna()

plt.plot(series)
plt.title("Original Time Series")
plt.show()

result = adfuller(series)
d = 0

if result[1] > 0.05:
    series = np.log(series)
    series = series.diff().dropna()
    d = 1

lags = min(10, len(series) // 2 - 1)

plot_acf(series, lags=lags)
plt.show()

plot_pacf(series, lags=lags, method="ywm")
plt.show()

p = 1
q = 1

model = ARIMA(df["Value"], order=(p, d, q))
fit = model.fit()

train = df["Value"][:-5]
test = df["Value"][-5:]

model = ARIMA(train, order=(p, d, q))
fit = model.fit()

predicted = fit.forecast(steps=len(test))

print("ARIMA Parameters:", (p, d, q))
print("MAE:", mean_absolute_error(test, predicted))
print("RMSE:", np.sqrt(mean_squared_error(test, predicted)))

plt.plot(test, label="Actual")
plt.plot(predicted, label="Predicted")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()

print("Forecast:")
print(fit.forecast(steps=5))
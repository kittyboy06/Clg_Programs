import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

data = df.select_dtypes(include=np.number)

data.plot(figsize=(10, 5))
plt.title("Multivariate Time Series")
plt.show()

for col in data.columns:
    print(col, "ADF p-value:", adfuller(data[col])[1])

stationary = data.diff().dropna()

n = int(len(stationary) * 0.8)
train = stationary[:n]
test = stationary[n:]

maxlags = min(5, len(train) // 3)
model = VAR(train)

lag = model.select_order(maxlags=maxlags).aic
print("Optimal Lag:", lag)

fit = model.fit(lag)

forecast = fit.forecast(train.values[-lag:], steps=len(test))
forecast = pd.DataFrame(forecast, index=test.index, columns=test.columns)

for col in test.columns:
    rmse = np.sqrt(mean_squared_error(test[col], forecast[col]))
    mae = mean_absolute_error(test[col], forecast[col])
    print(col, "RMSE:", round(rmse, 4), "MAE:", round(mae, 4))

for col in test.columns:
    plt.figure(figsize=(10, 4))
    plt.plot(test.index, test[col], label="Actual")
    plt.plot(forecast.index, forecast[col], label="Forecast")
    plt.title(col + " - Actual vs Forecast")
    plt.legend()
    plt.show()

print("Forecast:")
print(forecast)
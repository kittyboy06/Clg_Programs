import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
df = pd.read_csv("data_sales.csv")
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df.set_index("date", inplace=True)
plt.figure(figsize=(10,5))
plt.plot(df["revenue"], marker='o')
plt.title("Original Time Series")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
result = adfuller(df["revenue"])
print("ADF Statistic :", result[0])
print("p-value :", result[1])
df["Log_Revenue"] = np.log(df["revenue"])
df["Diff_Log"] = df["Log_Revenue"].diff()
diff_series = df["Diff_Log"].dropna()
result = adfuller(diff_series)
print("ADF Statistic after Differencing :", result[0])
print("p-value :", result[1])
plot_acf(diff_series)
plt.show()
plot_pacf(diff_series)
plt.show()
d = 1
model = ARIMA(df["revenue"], order=(1,1,1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=5)
print("Forecasted Values:")
print(forecast)
plt.figure(figsize=(10,5))
plt.plot(df.index, df["revenue"], label="Actual")
future_dates = pd.date_range(start=df.index[-1], periods=6, freq="D")[1:]
plt.plot(future_dates, forecast, marker='o', label="Forecast")
plt.title("Actual vs Forecast")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
plt.show()
predicted = model_fit.predict(start=1, end=len(df)-1)
actual = df["revenue"][1:]
rmse = np.sqrt(mean_squared_error(actual, predicted))
mae = mean_absolute_error(actual, predicted)
print("RMSE :", rmse)
print("MAE :", mae)
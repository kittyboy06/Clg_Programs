import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

data = pd.read_csv("D:\\KB06\\Clg_Programs\\5th Sem\\TSA\\data_sales.csv")

data["date"] = pd.to_datetime(data["date"])
data.set_index("date", inplace=True)

series = data["revenue"]

plt.figure(figsize=(10, 5))
plt.plot(series, label="Original Data")
plt.title("Original Time Series")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.show()

train = series[:-5]
test = series[-5:]

model = SimpleExpSmoothing(train)
fit = model.fit(optimized=True)

forecast = fit.forecast(len(test))

plt.figure(figsize=(10, 5))
plt.plot(train, label="Training Data")
plt.plot(test, label="Actual Test Data")
plt.plot(fit.fittedvalues, label="Smoothed Values")
plt.plot(forecast, label="Forecast", color="red")
plt.title("First-Order Exponential Smoothing")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.show()

mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("Smoothing Parameter (Alpha):", fit.model.params["smoothing_level"])
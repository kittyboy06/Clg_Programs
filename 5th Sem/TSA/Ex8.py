import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df = pd.read_csv("data.csv")

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

series = df["Value"].dropna()

n = int(len(series) * 0.8)
train = series[:n]
test = series[n:]

naive = np.repeat(train.iloc[-1], len(test))

mean_forecast = np.repeat(train.mean(), len(test))

model = SimpleExpSmoothing(train)
fit = model.fit()
exp_forecast = fit.forecast(len(test))

methods = {
    "Naive": naive,
    "Mean": mean_forecast,
    "Exponential Smoothing": exp_forecast
}

for name, forecast in methods.items():
    rmse = np.sqrt(mean_squared_error(test, forecast))
    mae = mean_absolute_error(test, forecast)
    print(name)
    print("RMSE:", round(rmse, 4))
    print("MAE:", round(mae, 4))
    print()

for name, forecast in methods.items():
    plt.figure(figsize=(10, 5))
    plt.plot(test.index, test, label="Actual")
    plt.plot(test.index, forecast, label=name)
    plt.title(name + " Forecast")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()
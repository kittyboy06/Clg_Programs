import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
series = df["Value"]

n = int(len(series) * 0.8)
train = series[:n]
test = series[n:]

naive = np.repeat(train.iloc[-1], len(test))
mean_pred = np.repeat(train.mean(), len(test))

model = SimpleExpSmoothing(train)
fit = model.fit()
exp_pred = fit.forecast(len(test))

methods = {
    "Naive": naive,
    "Mean": mean_pred,
    "Exponential Smoothing": exp_pred
}

for name, pred in methods.items():
    print(name)
    print("MAE:", mean_absolute_error(test, pred))
    print("RMSE:", np.sqrt(mean_squared_error(test, pred)))
    print()

for name, pred in methods.items():
    plt.figure()
    plt.plot(test.index, test, label="Actual")
    plt.plot(test.index, pred, label=name)
    plt.title(name + " Forecast")
    plt.legend()
    plt.show()

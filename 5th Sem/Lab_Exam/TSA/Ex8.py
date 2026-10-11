import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df = pd.read_csv("data.csv")

df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

df.set_index("date", inplace=True)
df = df.asfreq("MS")

series = df["Value"].astype(float).dropna()

n = int(len(series) * 0.8)
train = series.iloc[:n]
test = series.iloc[n:]

naive = np.repeat(train.iloc[-1], len(test))

mean_pred = np.repeat(train.mean(), len(test))

model = SimpleExpSmoothing(
    train.to_numpy(),
    initialization_method="estimated"
)

fit = model.fit()

exp_pred = np.asarray(fit.forecast(len(test)))

methods = {
    "Naive": naive,
    "Mean": mean_pred,
    "Exponential Smoothing": exp_pred
}

for name, pred in methods.items():
    mae = mean_absolute_error(test.to_numpy(), pred)
    rmse = np.sqrt(mean_squared_error(test.to_numpy(), pred))

    print(name)
    print("MAE:", round(mae, 4))
    print("RMSE:", round(rmse, 4))
    print()

for name, pred in methods.items():
    plt.figure(figsize=(10, 5))

    plt.plot(
        test.index, test.to_numpy(),
        marker="o", label="Actual"
    )

    plt.plot(
        test.index, pred,
        marker="x", linestyle="--", label=name
    )

    plt.title(name + " Forecast")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

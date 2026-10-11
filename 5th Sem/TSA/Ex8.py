import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df = pd.read_csv("data.csv")

date_col = next(
    (col for col in df.columns if col.lower() == "date"),
    None
)

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True)
    df.set_index(date_col, inplace=True)

series = pd.to_numeric(df["Value"], errors="coerce").dropna()

if len(series) < 2:
    raise ValueError("Dataset must contain at least two valid values.")

n = int(len(series) * 0.8)
n = max(1, min(n, len(series) - 1))

train = series.iloc[:n]
test = series.iloc[n:]

print("Training observations:", len(train))
print("Testing observations:", len(test))
print()

naive_forecast = np.repeat(train.iloc[-1], len(test))

mean_forecast = np.repeat(train.mean(), len(test))

model = SimpleExpSmoothing(
    train.astype(float),
    initialization_method="estimated"
)

fit = model.fit()
exp_forecast = fit.forecast(len(test))

methods = {
    "Naive Forecast": naive_forecast,
    "Mean Forecast": mean_forecast,
    "Exponential Smoothing": exp_forecast.to_numpy()
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

    plt.plot(
        test.index,
        test.to_numpy(),
        label="Actual Values",
        marker="o"
    )

    plt.plot(
        test.index,
        forecast,
        label="Predicted Values",
        marker="x"
    )

    plt.title(name + " - Actual vs Forecast")
    plt.xlabel("Date" if date_col else "Time Step")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
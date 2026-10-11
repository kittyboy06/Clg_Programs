import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv("2col.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

data = df.select_dtypes(include=np.number)

for col in data.columns:
    print(col, "ADF p-value:", adfuller(data[col])[1])

diff_data = data.diff().dropna()

n = int(len(diff_data) * 0.8)
train = diff_data[:n]
test = diff_data[n:]

model = VAR(train)
lag = model.select_order(maxlags=3).aic
fit = model.fit(lag)

forecast = fit.forecast(train.values[-lag:], steps=len(test)) # type: ignore
forecast_df = pd.DataFrame(forecast, index=test.index, columns=test.columns)

for col in test.columns:
    print(col, "MAE:", mean_absolute_error(test[col], forecast_df[col]))
    print(col, "RMSE:", np.sqrt(mean_squared_error(test[col], forecast_df[col])))

for col in test.columns:
    plt.figure()
    plt.plot(test.index, test[col], label="Actual")
    plt.plot(forecast_df.index, forecast_df[col], label="Forecast")
    plt.title(col + " Actual vs Forecast")
    plt.legend()
    plt.show()

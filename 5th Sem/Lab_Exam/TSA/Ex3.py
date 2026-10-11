import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
series = df["Value"]

plt.figure()
plt.plot(series, label="Original")
plt.title("Original Time Series")
plt.legend()
plt.show()

model = SimpleExpSmoothing(series)
fit = model.fit()
smoothed = fit.fittedvalues

plt.figure()
plt.plot(series, label="Original")
plt.plot(smoothed, label="Smoothed")
plt.title("Exponential Smoothing")
plt.legend()
plt.show()

print("MAE:", mean_absolute_error(series, smoothed))
print("RMSE:", np.sqrt(mean_squared_error(series, smoothed)))

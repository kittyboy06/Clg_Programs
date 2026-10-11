import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

plt.figure()
plt.plot(df["Value"])
plt.title("Time Series Plot")
plt.show()

plot_acf(df["Value"], lags=10)
plt.title("Autocorrelation Function (ACF)")
plt.show()

plot_pacf(df["Value"], lags=10)
plt.title("Partial Autocorrelation Function (PACF)")
plt.show()

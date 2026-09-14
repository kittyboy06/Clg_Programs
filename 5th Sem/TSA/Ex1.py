import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["date"])
df.set_index("Date", inplace=True)

series = df["Value"]

plt.figure(figsize=(10, 5))
sns.lineplot(x=series.index, y=series.values)
plt.title("Time Series Plot")
plt.xlabel("Date")
plt.ylabel("Value")
plt.show()

df["Month"] = df.index.month

plt.figure(figsize=(10, 5))
sns.boxplot(x=df["Month"], y=df["Value"])
plt.title("Seasonal Plot")
plt.xlabel("Month")
plt.ylabel("Value")
plt.show()

result = seasonal_decompose(series, model="additive", period=12)

result.plot()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

plt.figure()
sns.lineplot(data=df, x=df.index, y="Value")
plt.title("Time Series Plot")
plt.show()

df["Month"] = df.index.month
plt.figure()
sns.boxplot(data=df, x="Month", y="Value")
plt.title("Seasonal Plot")
plt.show()

result = seasonal_decompose(df["Value"], model="additive", period=12)
result.plot()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

plt.figure()
plt.plot(df["Value"])
plt.title("Original Time Series")
plt.show()

df["LogValue"] = np.log(df["Value"])
df["Diff"] = df["LogValue"].diff()
df["MA"] = df["Value"].rolling(window=3).mean()
df["Time"] = np.arange(len(df))

X = df[["Time"]]
y = df["LogValue"]

model = LinearRegression()
model.fit(X, y)

pred_log = model.predict(X)
pred = np.exp(pred_log)

plt.figure()
plt.plot(df.index, df["Value"], label="Actual")
plt.plot(df.index, pred, label="Predicted")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()

print("MAE:", mean_absolute_error(df["Value"], pred))
print("RMSE:", np.sqrt(mean_squared_error(df["Value"], pred)))

residuals = df["Value"] - pred
plt.figure()
plt.plot(df.index, residuals)
plt.axhline(0, color="r", linestyle="--")
plt.title("Residual Analysis")
plt.show()

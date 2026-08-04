import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv("data_sales.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df.set_index("date", inplace=True)

plt.figure(figsize=(10,5))
plt.plot(df.index, df["revenue"], marker='o')
plt.title("Original Time Series")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

df["Log_Revenue"] = np.log(df["revenue"])

df["Differenced"] = df["revenue"].diff()

df["Moving_Avg"] = df["revenue"].rolling(window=3).mean()

df["Time"] = np.arange(len(df))

X = df[["Time"]]
y = df["Log_Revenue"]

model = LinearRegression()
model.fit(X, y)

df["Predicted_Log"] = model.predict(X)

plt.figure(figsize=(10,5))
plt.plot(df.index, y, label="Actual Log Revenue", marker='o')
plt.plot(df.index, df["Predicted_Log"], label="Predicted Log Revenue", linestyle="--")
plt.title("Actual vs Predicted (Log Scale)")
plt.xlabel("Date")
plt.ylabel("Log Revenue")
plt.legend()
plt.grid(True)
plt.show()

rmse = np.sqrt(mean_squared_error(y, df["Predicted_Log"]))
mae = mean_absolute_error(y, df["Predicted_Log"])

print("RMSE:", rmse)
print("MAE :", mae)

df["Residuals"] = y - df["Predicted_Log"]

plt.figure(figsize=(10,5))
plt.plot(df.index, df["Residuals"], marker='o')
plt.axhline(0, color='red', linestyle='--')
plt.title("Residual Analysis")
plt.xlabel("Date")
plt.ylabel("Residuals")
plt.grid(True)
plt.show()

df["Predicted_Revenue"] = np.exp(df["Predicted_Log"])

print("\nActual vs Predicted Revenue")
print(df[["revenue", "Predicted_Revenue"]])

plt.figure(figsize=(10,5))
plt.plot(df.index, df["revenue"], label="Actual Revenue", marker='o')
plt.plot(df.index, df["Predicted_Revenue"], label="Predicted Revenue", linestyle='--')
plt.title("Actual vs Predicted Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
plt.show()
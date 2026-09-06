import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf

df = pd.read_csv("data.csv")

print("Dataset:")
print(df.head())

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

series = df["Value"].dropna()

lags = min(20, len(series) // 2 - 1)

plt.figure(figsize=(10, 5))
plt.plot(series)
plt.title("Time Series Plot")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.show()

fig, ax = plt.subplots(figsize=(10, 5))
plot_acf(series, lags=lags, alpha=0.05, ax=ax)
ax.set_title("Autocorrelation Function (ACF)")
ax.set_xlabel("Lag")
ax.set_ylabel("Autocorrelation")
plt.show()

fig, ax = plt.subplots(figsize=(10, 5))
plot_pacf(series, lags=lags, alpha=0.05, method="ywm", ax=ax)
ax.set_title("Partial Autocorrelation Function (PACF)")
ax.set_xlabel("Lag")
ax.set_ylabel("Partial Autocorrelation")
plt.show()

acf_values, acf_confint = acf(series, nlags=lags, alpha=0.05)

print("\nSignificant ACF Spikes:")
for lag in range(1, len(acf_values)):
    lower = acf_confint[lag, 0]
    upper = acf_confint[lag, 1]

    if acf_values[lag] < lower or acf_values[lag] > upper:
        print("Lag", lag, ":", round(acf_values[lag], 4))

pacf_values, pacf_confint = pacf(
    series,
    nlags=lags,
    alpha=0.05,
    method="ywm"
)

print("\nSignificant PACF Spikes:")
for lag in range(1, len(pacf_values)):
    lower = pacf_confint[lag, 0]
    upper = pacf_confint[lag, 1]

    if pacf_values[lag] < lower or pacf_values[lag] > upper:
        print("Lag", lag, ":", round(pacf_values[lag], 4))

print("\nInterpretation:")
print("ACF spikes outside the 95% confidence interval indicate significant autocorrelation.")
print("PACF spikes outside the 95% confidence interval indicate significant direct relationships.")

print("\nProgram completed successfully.")
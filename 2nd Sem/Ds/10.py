import pandas as pd
import matplotlib.pyplot as plt
import yfinance
data = yfinance.download("GOOGL", start="2023-01-01", end="2023-03-01",auto_adjust=False)
print(data.head())
plt.figure(figsize=(10, 5))
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.title("Alphabet Inc. (GOOGL)")
plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
plt.legend()
plt.grid(True)
plt.show()
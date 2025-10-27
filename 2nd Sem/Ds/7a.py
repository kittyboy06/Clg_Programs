import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv"
data = pd.read_csv(path)
cols = data.columns.tolist()
print(cols)
parameter = input("Enter the parameter name: ")
while parameter not in cols:
    parameter = input("Enter the correct parameter name: ")
value = data[parameter]
mean = value.mean()
std_dev = value.std()
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-(x - mean) ** 2 / (2 * std_dev ** 2))
plt.title(f'Normal Distribution for {parameter} in UCI Dataset')
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.show()
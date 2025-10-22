import pandas as pd
import matplotlib.pyplot as plt

path ="C:\\Users\\Admin\\Downloads\\diabetes[1].csv"
data = pd.read_csv(path)

x = data['Age']
y = data['BMI']

correlation_coefficient = x.corr(y)

plt.scatter(x, y, marker='x', color = 'red')
plt.xlabel('AGE')
plt.ylabel('BMI')
plt.title('Scatter Plot: AGE vs. BMI')

plt.text(x.min(), y.max(), f'Correlation: {correlation_coefficient:.2f}', ha='left', va='top')

plt.show()

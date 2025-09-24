import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Sine Wave')
plt.title('Line Chart')
plt.xlabel('X')
plt.ylabel('sin(X)')
plt.legend()
axs[0, 0].grid(True)
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True)
x_scatter = np.random.rand(10)
y_scatter = np.random.rand(10)
plt.scatter(x_scatter, y_scatter, color='green')
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
sizes = [30, 20, 25, 25]
labels = ['Apple', 'Banana', 'Cherry', 'Date']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')

plt.tight_layout()
plt.show()

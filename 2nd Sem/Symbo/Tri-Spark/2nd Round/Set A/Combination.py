import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
x = np.linspace(0, 10, 100)
y = np.sin(x)
axs[0, 0].plot(x, y, label='Sine Wave')
axs[0, 0].set_title('Line Chart')
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('sin(X)')
axs[0, 0].legend()
axs[0, 0].grid(True)

categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
axs[0, 1].bar(categories, values, color='skyblue')
axs[0, 1].set_title('Bar Chart')
axs[0, 1].set_xlabel('Category')
axs[0, 1].set_ylabel('Value')
axs[0, 1].grid(True)

x_scatter = np.random.rand(10)
y_scatter = np.random.rand(10)
axs[1, 0].scatter(x_scatter, y_scatter, color='green')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('X')
axs[1, 0].set_ylabel('Y')
axs[1, 0].grid(True)

sizes = [30, 20, 25, 25]
labels = ['Apple', 'Banana', 'Cherry', 'Date']
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title('Pie Chart')

fig.tight_layout()
plt.show()

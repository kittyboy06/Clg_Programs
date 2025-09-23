import matplotlib.pyplot as plt
import numpy as np

# Generating data
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Creating contour plot
plt.contour(X, Y, Z)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Contour Plot')

# Displaying the plot
plt.show()

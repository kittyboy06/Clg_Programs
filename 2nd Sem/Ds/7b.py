import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde, gaussian_kde

path = "D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv"
data = pd.read_csv(path)

col_names = data.columns.tolist()
print('The available fields:', col_names)
x = data[input("Enter parameter 1")]
y = data[input("Enter parameter 2")]

x_grid, y_grid = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))
grid_points = np.vstack([x_grid.ravel(), y_grid.ravel()])

kde_estimator = gaussian_kde([x, y])
density_values = kde_estimator(grid_points)

density_values = density_values.reshape(x_grid.shape)

plt.figure()
plt.imshow(density_values.T, origin='lower', aspect='auto', extent=[min(x), max(x), min(y), max(y)])
plt.colorbar(label='Density')
plt.scatter(x, y, color='red', alpha=0.5, label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Density Plot')
plt.legend()
plt.show()

plt.figure()
plt.contour(x_grid, y_grid, density_values, levels=10, cmap='viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot')
plt.legend()
plt.show()
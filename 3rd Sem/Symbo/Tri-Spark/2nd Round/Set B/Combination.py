import numpy as np

import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

x1 = [0,6,11,8.5,3]
x2 = [0,10,10,0,0,10]
y4 = [0,10,0,5,5]
y5 = [0,0,5,5,10,10]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x1, y4, 'b-', label='sin(x)')
axs[0, 0].set_title('A')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(x2, y5, 'r-', label='cos(x)')
axs[0, 1].set_title('S')
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(x, y3, 'g-.', label='tan(x)')
axs[1, 0].set_ylim(-5, 5)
axs[1, 0].set_title('Tangent Wave (limited)')
axs[1, 0].legend()
axs[1, 0].grid(True)

colors = np.sqrt(x)
scatter = axs[1, 1].scatter(x, y1 + y2, c=colors, cmap='viridis')
axs[1, 1].set_title('Scatter: sin(x) + cos(x)')
fig.colorbar(scatter, ax=axs[1, 1], label='sqrt(x)')
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()
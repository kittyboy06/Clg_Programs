import numpy as np

import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# First subplot: Sine wave
axs[0, 0].plot(x, y1, 'b-', label='sin(x)')
axs[0, 0].set_title('Sine Wave')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Second subplot: Cosine wave
axs[0, 1].plot(x, y2, 'r--', label='cos(x)')
axs[0, 1].set_title('Cosine Wave')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Third subplot: Tangent wave with limits
axs[1, 0].plot(x, y3, 'g-.', label='tan(x)')
axs[1, 0].set_ylim(-5, 5)
axs[1, 0].set_title('Tangent Wave (limited)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Fourth subplot: Scatter plot with color mapping
colors = np.sqrt(x)
scatter = axs[1, 1].scatter(x, y1 + y2, c=colors, cmap='viridis')
axs[1, 1].set_title('Scatter: sin(x) + cos(x)')
fig.colorbar(scatter, ax=axs[1, 1], label='sqrt(x)')
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()
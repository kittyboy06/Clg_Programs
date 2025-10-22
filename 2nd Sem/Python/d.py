import numpy as np

a = np.array([1, 8, 5, 9, 6, 7, 12, 3])
x1, x2, x3 = np.split(a, [3, 5])
print(x1, "\n", x2, "\n", x3)
x4, x5, x6 = np.split(a, [3, 8])
print("\n", x4, x5, x6)
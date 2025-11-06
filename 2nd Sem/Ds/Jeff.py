import numpy as np
import pandas as pd

a = np.array([[1, 2, 3], [4, 5, 6]])
print("From NumPy Array:\n", pd.DataFrame(a), "\n")

d = {'A': [1, 2], 'B': [3, 4]}
print("From Dictionary:\n", pd.DataFrame(d), "\n")

s = pd.Series({'India': 'New Delhi', 'US': 'Washington'})
print("From Series:\n", pd.DataFrame(s), "\n")

df = pd.DataFrame(a)
print("Shape:", df.shape)
print("Index Length:", len(df.index))
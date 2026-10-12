import numpy as np

A = np.array([[4, 7, 2], [3, 6, 1], [2, 5, 8]])
B = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Multiplication:\n", A @ B)
print("Inverse of A:\n", np.linalg.inv(A))
print("Transpose of A:\n", A.T)
print("Row Min:", A.min(axis=1), "| Row Max:", A.max(axis=1))
print("Col Min:", A.min(axis=0), "| Col Max:", A.max(axis=0))
print("Matrix Min:", A.min(), "| Matrix Max:", A.max())
print("Trace of A:", np.trace(A))
print("Rank of A:", np.linalg.matrix_rank(A))

# Program 01: Matrix Operations using NumPy
import numpy as np

# Define two 3x3 matrices
A = np.array([[4, 7, 2], [3, 6, 1], [2, 5, 8]])
B = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# 1. Addition, Subtraction, Multiplication
print("\nAddition (A + B):\n", A + B)
print("\nSubtraction (A - B):\n", A - B)
print("\nMultiplication (A @ B):\n", A @ B)

# 2. Matrix Inversion
print("\nInverse of A:\n", np.linalg.inv(A))

# 3. Transpose
print("\nTranspose of A:\n", A.T)

# 4. Min and Max of each row and each column
print("\nRow-wise Min:", np.min(A, axis=1))
print("Row-wise Max:", np.max(A, axis=1))
print("Column-wise Min:", np.min(A, axis=0))
print("Column-wise Max:", np.max(A, axis=0))

# 5. Min and Max of the entire matrix
print("\nMatrix Min:", np.min(A))
print("Matrix Max:", np.max(A))

# 6. Trace and Rank
print("\nTrace of A:", np.trace(A))
print("Rank of A:", np.linalg.matrix_rank(A))

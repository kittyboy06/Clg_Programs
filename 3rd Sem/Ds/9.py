import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1,2,3,4,5])
result = np.array_equal(a1, a2)
print("Arrays are equal:", result)
Element_wise_comparison = a1 == a2
print("Element-wise comparison:", Element_wise_comparison)
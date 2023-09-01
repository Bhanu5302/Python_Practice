"""NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy arrays are 50x faster than lists, because stores the values in continous memory locations
"""
import numpy as np

# ----use 1D array
arr = np.array([1, 2, 3, 4])
print(arr)
print(np.__version__)

# ----use 2D array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)

# ----use 3D array
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2)
print(arr2[1])

# checking the Number of dimensions in array
print(arr1.ndim)
print(arr2.ndim)

# ------indexing arrays-------
print(arr[2] + arr[1])  # adding index values of array
print(arr2[1, 0])  # printing 1st array in 2nd row
print(arr2[1,-1])   # negative indexing last row

# -----

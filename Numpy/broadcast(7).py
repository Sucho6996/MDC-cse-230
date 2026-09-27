# Broadcasting in NumPy is a powerful mechanism 
# that allows arithmetic operations to be performed 
# on arrays of different shapes. 
# Instead of creating costly copies of data 
# in memory, NumPy virtually stretches the 
# smaller array across the larger array so that 
# they have compatible shapes for element-wise 
# operations.

# The dimensions have the same size
# OR
# One of the dimensions has a size of 1

import numpy as np

arr1=np.array([[1,2,3,4]])
arr2=np.array([[1],[2],[3],[4]])

print(arr1.shape)
print(arr2.shape)

print(arr1+arr2)

arr1=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])

print(arr1.shape)
print(arr2.shape)

print(arr1+arr2)

# Exercise: create a 10/10 multiplication table 
# using broadcast


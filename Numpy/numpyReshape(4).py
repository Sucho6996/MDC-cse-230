# reshape() = Changes the shape of an array
#             w/o altering its underlying data
#             .reshape(Layers,rows, columns)

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("\nArray: \n",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

arr=arr.reshape(3,4)
print("\nArray: \n",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

arr=arr.reshape(2,2,3)
print("\nArray: \n",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

#Try out negative dimension
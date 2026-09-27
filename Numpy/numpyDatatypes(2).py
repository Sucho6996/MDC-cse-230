#Learn dtype first
#int (8,16,32,64)
#float (16,32,64)
#boolean (bool_) '_' for numpy boolean
#string (str_,<U#) '_' for numpy boolean
#object (object_) use python object for custom classes and pandas

import numpy as np

arr=np.array([1,2,3,4,5])

print("Array = ",arr)
print("Data Type = ", arr.dtype)
print("Storage required : ",arr.nbytes," bytes")

arr=np.array([1,2,3,4,5],dtype=np.int32)

print("\n\nAfter setting the dtype manually")
print("Array = ",arr)
print("Data Type = ", arr.dtype)
print("Storage required : ",arr.nbytes," bytes")

arr=arr.astype(np.float16)
print("\n\nAfter typecast the dtype manually")
print("Array = ",arr)
print("Data Type = ", arr.dtype)
print("Storage required : ",arr.nbytes," bytes")

#Learn the Min and Max value for each dtype 
# and explore other dtype as well

fruits=np.array(["Apple","Orange","Banana","Chiku"], dtype="str_")
print("\n\nAfter setting the dtype manually")
print("Array = ",fruits)
print("Data Type = ", fruits.dtype)
print("Storage required : ",fruits.nbytes," bytes")



import numpy as np

# Aggreagte functions summarize data
# and return a single value

arr=np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20]])

print("Array:\n",arr)

print("Sum = ",np.sum(arr))
print("Avg = ",np.mean(arr))
print("Varriation = ",np.var(arr))
print("Std = ",np.std(arr))

# .min(), .max(), -> try out by yourself

print("Position of min = ",np.argmin(arr))
print("Position of max = ",np.argmax(arr))

print("Sum of cols = ",np.sum(arr,axis=0))
print("Sum of rows = ",np.sum(arr,axis=1))
import numpy as np

arr1=np.array([[1,2,3],
              [4,5,6]])

arr2=np.array([[10,20,30],
              [40,50,60]])

np.save("data",arr1)
np.savez("datas",arr1,arr2)
#np.savez_compresse() -> try by yourself

print("NumPy array saved successfully!!")
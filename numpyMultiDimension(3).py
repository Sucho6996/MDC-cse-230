import numpy as np

arr=np.array('A') # 0 dimension
print("\nArray: ",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

arr=np.array(['A','B','C']) # 1 dimension
print("\nArray: ",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

arr=np.array([['A','B','C'],
              ['D','E','F'],
              ['G','H','I']
            ]) # 2 dimension
print("\nArray: \n",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)

arr=np.array([
            [['A','B','C'],['D','E','F'],['G','H','I']],
            [['J','K','L'],['M','N','O'],['P','Q','R']],
            [['S','T','U'],['V','W','X'],['Y','Z','_']]
              ]) # 3 dimension
print("\nArray: \n",arr)
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)
#Try upto N dimension 


#In List we have learn chain indexing
#like to access t -> arr[2][0][1]
#But in numpy we can use multidimensional Indexing

print("Accessing 'T' through multidimensionl Indexing -> ",arr[2,0,1])

#Assignment: Create five 3 letter words using indexing


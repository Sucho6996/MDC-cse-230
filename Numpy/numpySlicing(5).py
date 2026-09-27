import numpy as np


#<-------------ROW SELECTION------------->
arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],#-2
    [13,14,15,16] #-1
])
print(arr,"\n")

# array[start:end:step] -> selecting the range

#for 2nd row
print("\n\n2nd Row")
print(arr[1:4:2])

#negative indexing
#print 2nd last row

print("\n\nRow Negative indexing: ")
print(arr[-2])


print("\n\nAll Rows: ")
print(arr[::2])

print("\n\nAll Rows Reversed: ")
print(arr[::-1]) #Try use -2 here

#<-------------COLOMN SELECTION------------->

print("\n\n2nd Col")
print(arr[:,1]) #try for all other colomn

print("\n\nCol Negative indexing: ")
print(arr[:,-3])

print("\n\nCol Range indexing: ")
print(arr[:,1::2])

print("\n\nAll Cols Reversed: ")
print(arr[:,::-1]) #Try use -2 here


#<-------------ROW-COL SELECTION------------->

print("\n\nRowCol Range indexing: ")
print(arr[0:2,0:2])

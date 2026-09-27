import numpy as np

#.zeroes(dim,row,col)
arr=np.zeros(10)
print("1d:\n",arr)
arr=np.zeros([2,10])
print("2d:\n",arr)
arr=np.zeros([2,3,10])
print("3d:\n",arr)

#.ones(dim,row,col)
arr=np.ones(10)
print("1d:\n",arr)
arr=np.ones([2,10])
print("2d:\n",arr)
arr=np.ones([2,3,10])
print("3d:\n",arr)

#.full((dim,row,col),val)
arr=np.full([2,3,10],9)
print("3d:\n",arr)

#.eye(shape) -> for linear algebra
arr=np.eye(2)
print("Eye = 2: \n",arr)

arr=np.eye(3)
print("Eye = 3: \n",arr)

#.empty(shape) -> try by yourself

#.arange(start, stop, step)
arr=np.arange(0,100,2) # start stop step
print(arr)

#.linspace(start, stop, num)-> try by yourself
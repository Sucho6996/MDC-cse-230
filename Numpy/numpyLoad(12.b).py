import numpy as np

print("Single array load:\n",np.load("data.npy"))

arrays=np.load("datas.npz")
print("Multiple array load:\n",arrays["arr_0"],"\n",arrays["arr_1"])
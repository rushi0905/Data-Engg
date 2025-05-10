import numpy as np
from numpy.ma.core import array

# array_Data = np.array([[1,2,3],[3,2,1],[4,5,6]])
# np.savetxt("first.csv",array_Data,delimiter=',',fmt='%d')

res = np.loadtxt("first.csv",delimiter=',',dtype=int)
print(res)
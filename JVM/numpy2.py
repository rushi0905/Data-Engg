import numpy as np
arr = np.arange(0,101,10)
print(arr)

print("*****************************************************************************************")

matx1 = np.array([[1,2,3]])
matx2 = np.array([[2,3,4]])
matx1_pow = np.power(matx1, 2)
matx2_pow = np.power(matx2, 2)

print("add",matx1+matx2)
print("mul",matx1*matx2)
print("sub",matx1-matx2)
print("div",matx1/matx2)

print("*****************************************************************************************")


angles = np.array([0,np.pi/2,np.pi])
result = np.sin(angles)
result1 = np.cos(angles)
print(result)
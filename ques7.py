import numpy as np
arr1=np.array([[1,2,3],
              [3,2,6],
              [4,3,1],
              [5,8,9]])

print(arr1)

A=np.ones((4,3))
B=np.zeros((2,3))
result=np.concatenate([A,B],axis=0)
print(result)
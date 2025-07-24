import numpy as np
a=np.array([[4,5,6],[1,2,3], [7, 8, 9]])
b=np.array([[4,5,6],[1,2,3], [7, 8, 9]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(np.dot(a,b))
print(np.cross(a,b))
print(a.T)
print(np.linalg.det(a))
print(np.linalg.inv(a))




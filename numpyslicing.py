import numpy as np
#One dimensional arrray slicing 
n1=np.array([12,8,9,34,67,90,33,29,45])
print(len(n1))
print(n1[:8])
print(n1[2:8])
print(n1[:])
print(n1[1:])
print(n1[::2])
print(n1[::-1])
print(n1[1:6:3])

#Two dimensional arrray slicing 
n2=np.array([[10,4,2,4,5],[11,98,65,34,9],[12,33,90,6,11],[99,77,33,22,10]])
print(n2)
print(n2.ndim)
print(n2[0,1:3])
print(n2[1,::-1])
print(n2[1:3,::-1])
print(n2[::-1,1:4:2])

#Three dimensional arrray slicing 
n3=np.array([[[11,22,33,44,55,66],[10,9,4,5,6,1],[10,3,8,2,4,8]],
              [[9,7,8,4,3,2],[11,33,44,55,22,76],[12,34,45,56,7,8]],
              [[11,7,23,45,78,5],[9,8,7,6,5,4],[22,33,44,55,66,77]]])
print(n3)
print("______")
print(n3[2,::,::])
print(n3[2,::-1,::-1])
print(n3[:3,0:3:2,0:5:3])
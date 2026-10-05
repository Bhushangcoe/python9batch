import numpy as np 

n1=np.array([8,6,4,5])
n2=np.array([10,43,12,6])
n=np.array([44,21,3,7])
n3=np.concatenate((n1,n2,n),axis=0)
print(n1) 
print(n2)
print(n)
print(n3)
print('-------------------------two dimensional---------------------------')
arr1=np.array([[11,76,32],[43,56,76],[34,9,8]])
arr2=np.array([[90,87,56],[12,32,35],[6,8,45]])
arr3=np.concatenate((arr1,arr2),axis=1)
print(arr3)
print('-------------------------three dimensional---------------------------')
a=np.array([[[8,9,6,5],[3,4,5,6],[23,5,6,8]],
            [[10,6,4,3],[2,6,9,8],[6,5,4,3]]])
b=np.array([[[10,6,4,5],[8,7,6,5],[33,65,21,8]],
            [[33,88,5,6],[2,3,4,5],[8,7,6,5]]])
c=np.concatenate((a,b),axis=2)
print(c) 
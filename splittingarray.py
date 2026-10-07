import numpy as np

num=np.array([10,22,3,4,5,6,23,8,7,65,43,23,12])
print('size=',len(num))
print(num)
n=np.array_split(num,8)
print(n)
# print(n[0])
num2=np.array([[10,22],[3,4],[5,6],[23,8],[7,65],[43,23]])
print(np.array_split(num2,4))

num=np.array([10,20,30,40,50,34,67,87,56,32])
print(np.where(num==20))
print(np.where(num>60))
print(np.where(num%2==0))
print(np.sort(num))
print(np.sort(num)[::-1])
print(num[::-1])
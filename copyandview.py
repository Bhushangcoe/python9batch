import numpy as np

n1=np.array([44,33,22,11])
copyn1=n1.copy()
print(n1)
print(copyn1)
n1[3]=90
copyn1[2]=40
print(n1)
print(copyn1)
print('------------view--------')
arr1=np.array([55,99,33,22,10])
arr1view=arr1.view()
print(arr1)
print(arr1view)
arr1[1]=100
arr1view[4]=30
print(arr1)
print(arr1view)
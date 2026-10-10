from numpy import random
n1=random.randint(30,50,size=(4))
n1=random.randint(30,50,size=(4,3))
n1=random.randint(30,50,size=(2,4,3))
print(n1)

n2=random.rand(3,2,6)
print(n2)

n3=random.choice([20,40,50,60,10])
n3=random.choice([20,40,50,60,10],p=[0.1,0.2,0.3,0.4,0.0],size=(10))
n3=random.choice([20,40,50,60,10],size=(2,3))
n3=random.choice([20,40,50,60,10],size=(2,3,3))

print(n3)
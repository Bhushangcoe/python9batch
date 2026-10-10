import numpy as np

num = np.array([32, 87, 56, 43, 90, 12, 42, 66, 90, 45])

# Filter 1: manual True/False list (must have exactly 10 values, one per element)
firstfilter = [True, False, True, True, False, True, False, True, False, True]
newarr = num[firstfilter]
print(num)
print(firstfilter)
print(newarr)

# Filter 2: build the True/False list with a loop
greaterthan50 = []
for i in num:
    if i > 50:
        greaterthan50.append(True)
    else:
        greaterthan50.append(False)

print(greaterthan50)
newarr2 = num[greaterthan50]
print(newarr2)
import pandas as pd

df=pd.read_csv('employee.csv')
print(df.info())
print("________________")
print(df)
print("________________")
print(df.head(3))
print("________________")
print(df.tail(5))
print("________________")

print(df.describe())
print("________________")

print(df.duplicated())
print("________________")

print(df.isna())
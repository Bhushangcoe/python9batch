import pandas as pd

df=pd.read_csv('customer_messydata.csv')
print(df)
print("________________")

print(df.duplicated())
# print(df.isna())
df.drop_duplicates(inplace=True)
print("_________drop duplicate_______")
print(df)
df.to_csv('customer_cleandata.csv', index=False)



import pandas as pd
import numpy as np

df = pd.read_csv('customer_cleandata.csv')
print(df['Age'])

# convert whole column to numbers (bad values become NaN)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# set a single cell (if you really need it)
# df.loc[4, 'Age'] = 0

print(df['Age'].isna())

# fill missing ages with 30
df['Age'] = df['Age'].fillna(30)

# negative ages are invalid -> make them NaN, then fill with the mean
df.loc[df['Age'] < 0, 'Age'] = np.nan
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df['Age'])
# print(df['Email'])
# df=df.dropna(subset=['Email'])
# print(df['Email'])
# df=df.dropna(subset=['Phone'])
# print(df['Phone'])
# df['City']=df['City'].fillna('Pune',inplace=True)
# print(df)
df['Salary']=df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df['Salary'])
df.loc[df['Salary']<0,'Salary']=df['Salary'].max()
print(df['Salary'])
df.to_csv('cdata.csv')
import pandas as pd

x = [10, 20, 30, 40, 50, 60]
s = pd.Series(x, index=['A', 'B', 'C', 'D', 'X', 'Y'])
print(x)
print(s)
print(s.loc['D'])

data = {
    'Rollno': [1, 2, 3, 4, 5, 6, 7],
    'Name': ['Priya', 'Raj', 'Pooja', 'Yash', 'Sakshi', 'Neha', 'Harshada'],
    'Marks': [87, 90, 67, 78, 54, 56, 88],
}
s2 = pd.Series(data)
print(s2)
print('----------------------------')
df = pd.DataFrame(data,index=['s1','s2','s3','s4','s5','s6','s7'])
print(df)
# print(df.loc[3])
# print(df.loc[[2,4,6]])
print(df.loc['s3']) #record/row
print(df.loc[['s1','s5','s7']])
print(df['Name']) #column
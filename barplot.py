import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('employee.csv')

# df.plot(x='department',y='salary',kind='bar',color='blue',title='BAR')
# df.plot(x='department',y='salary',kind='barh',color='black',title='BARH')
# df.plot(x='eid', y='salary', kind='scatter', color='blue', title='SCATTER',
#         s=40, alpha=0.5, marker='s', edgecolors='red')
df.plot(y='salary', labels=df['department'], kind='pie', title='PIE',
        autopct='%1.1f%%', legend=False)
plt.show()  

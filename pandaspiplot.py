import pandas as pd
import matplotlib.pyplot as plt

data={
    "expense":['rent','food','travel','shopping','saving'],
    "amount":[5000,2000,4000,10000,1000]
}

df = pd.DataFrame(data)

df.plot(y='amount', labels=df['expense'], kind='pie', title='EXPENSES',
        autopct='%1.1f%%', legend=False)
plt.ylabel('')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":["sneha","raj","rahul","yash","nikita","sakshi","rutuja","tushar"],
    "Marks":[85,78,67,56,89,77,89,70]
}

df=pd.DataFrame(data)
print(df)
df.plot(x="Name",y="Marks",kind="line",color='red',grid=True,title='Result',
        linestyle='solid',linewidth=2,marker='P')
plt.show()
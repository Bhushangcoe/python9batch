import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python9'
)
c=conn.cursor()
# query="select * from employee where salary>=40000"
# query="select * from employee where department='testing'"
query="select * from employee order by name"

c.execute(query)
data=c.fetchall()
print(c.rowcount)
# print(data)
for record in data:
    print(record)
c.close()
conn.close()
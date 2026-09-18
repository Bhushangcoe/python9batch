import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python9'
)
c=conn.cursor()
# query="update employee set salary=60000 where eid=103"
query="update employee set salary=%s where eid=%s"
salary=int(input('Enter salary='))
id=int(input('Enter Employee ID='))
value=(salary,id)
c.execute(query,value)
# c.execute(query)
conn.commit()
print(c.rowcount,'record Updated')
c.close()
conn.close()
import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python9'
)
c=conn.cursor()
query="delete from employee where eid=%s"
id = input("Enter employee id to delete: ")
c.execute(query, (id,))
conn.commit()
print(c.rowcount,'record deleted')
c.close()
conn.close()
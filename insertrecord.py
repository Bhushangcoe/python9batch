import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python9'
)
c=conn.cursor()
query="insert into employee values(%s,%s,%s,%s)"
value=[
    (102,'Riya','Testing',30000),
    (103,'Siya','HR',40000),
    (104,'vishal','Devops',60000),
    (105,'rajesh','Testing',76000),
    (106,'yash','Data science',89000)
    ]
c.executemany(query,value)
conn.commit()
print(c.rowcount,'record inserted')
c.close()
conn.close()
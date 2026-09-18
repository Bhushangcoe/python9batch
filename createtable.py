import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python9"
)

#create a cursor object
c=conn.cursor()
c.execute("create table employee (eid int , name varchar(20),department varchar(20), salary int)")
print("Table created successfully")
c.close()
conn.close()
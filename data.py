import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)

#create a cursor object
c=conn.cursor()
c.execute("create database python9")
c.close()
conn.close()
#fetch all rows from the executed query 
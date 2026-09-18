import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python9'
)

# Create cursor
c = conn.cursor()

# SQL query
query = "SELECT * FROM employee ORDER BY name"

# Execute query
c.execute(query)

# Fetch all records
data = c.fetchall()

# Display number of records
print("Total records:", c.rowcount)

# Display records
for record in data:
    print(record)

# Close cursor and connection
c.close()
conn.close()
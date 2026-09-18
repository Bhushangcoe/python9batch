import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python9'
)

c = conn.cursor()

# Create temporary table containing only unique rows
c.execute("""
CREATE TEMPORARY TABLE employee_unique AS
SELECT DISTINCT *
FROM employee
""")

# Delete all records from employee
c.execute("DELETE FROM employee")

# Insert unique records back
c.execute("""
INSERT INTO employee
SELECT *
FROM employee_unique
""")

conn.commit()

print("Duplicate records deleted successfully!")

c.close()
conn.close()
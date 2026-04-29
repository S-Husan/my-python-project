import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='Husan',
    password='1234',
    database='suit'
)

if conn.is_connected():
    print("Connected")
else:
    print("Not connected")

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

result = cursor.fetchall()

for row in result:
    print(row)
    
    
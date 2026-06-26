import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_DB_PASSWORD",
    database="attendance_system"
)

cursor = db.cursor()

print("Database Connected Successfully")
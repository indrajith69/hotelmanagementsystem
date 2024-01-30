import mysql.connector
from datetime import date


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="hotelmanagementsystem"
)

mycursor = mydb.cursor()

def test():
    mycursor.execute("SELECT * FROM GUESTS")
    print(mycursor.fetchone())
    
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Bali' WHERE address = 'Jl. Bali 5'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
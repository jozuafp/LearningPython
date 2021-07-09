import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (id, name, fav) VALUES (%s, %s, %s)"
val = [
  (1, 'John', 154),
  (2, 'Peter', 154),
  (3, 'Amy', 155),
  (4, 'Hannah', ''),
  (5, 'Michael', '')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
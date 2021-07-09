import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(255))")

sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
  (154, 'Chocolate Heaven'),
  (155, 'Tasty Lemons'),
  (156, 'Vanilla Dreams')
]

#mycursor = mydb.cursor()

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
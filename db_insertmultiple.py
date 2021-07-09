import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Jl. Tidar 100'),
  ('Amy', 'Jl. Kalimantan 12'),
  ('Hannah', 'Jl. Bali 5'),
  ('Michael', 'Jl. Sumatra 75'),
  ('Sandy', 'Malang'),
  ('Betty', 'Bandung'),
  ('Richard', 'Surabaya'),
  ('Susan', 'Sidoarjo'),
  ('Vicky', 'Yogyakarta'),
  ('Ben', 'Semarang'),
  ('William', 'Salatiga'),
  ('Chuck', 'Bangkalan'),
  ('Viola', 'Magelang')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
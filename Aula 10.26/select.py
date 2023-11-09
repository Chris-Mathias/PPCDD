import mysql.connector
import banco

conn = banco.getConexao()
cursor = conn.cursor()

sql = "SELECT * FROM cliente"
cursor.execute(sql)

resultado = cursor.fetchall()
print(type(resultado))
print(resultado)

print("\n")

for x in resultado:
    print(x)

conn.close()
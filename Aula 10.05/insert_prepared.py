import banco

con = banco.getConexao()
cursor = con.cursor(prepared=True)

sql = "INSERT INTO cliente (id_cliente, nome_cliente, id_tipo_cliente) VALUES (default, %s, %s)"
par = ("Chris", 5)

cursor.execute(sql, par)

con.commit()

print(cursor.rowcount, "registro(s) inserido(s).")
print("ID:", cursor.lastrowid)

con.close()
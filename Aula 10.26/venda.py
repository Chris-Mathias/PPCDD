import banco

conn = banco.getConexao()
cursor = conn.cursor()

# VENDA

def novaVenda(id_vendedor, id_cliente, dt_venda):

    sql = "INSERT INTO venda (id_venda, id_vendedor, id_cliente, dt_venda) VALUES (default, %s, %s, %s)"
    x = (id_vendedor, id_cliente, dt_venda)
    cursor.execute(sql, x)
    id_venda = cursor.lastrowid
    return id_venda

# ITEM VENDA

def novoItemVenda(id_venda, id_grupo, id_item, qtde):

    sql = "INSERT INTO item_venda (id_venda, id_grupo, id_item, qtde) VALUES (%s, %s, %s, %s)"
    x = (id_venda, id_grupo, id_item, qtde)
    cursor.execute(sql, x)

    sql = "SELECT preco FROM item WHERE id_grupo = %s AND id_item = %s"
    x = (id_grupo, id_item)
    cursor.execute(sql, x)
    preco = cursor.fetchone()

    valor = preco[0]*qtde

    sql = "UPDATE item_venda SET valor = %s WHERE id_venda = %s AND id_grupo = %s AND id_item = %s"
    x = (valor, id_venda, id_grupo, id_item)
    cursor.execute(sql, x)

    sql = "UPDATE item SET qtde_estoque = qtde_estoque - %s WHERE id_grupo = %s AND id_item = %s"
    x = (qtde, id_grupo, id_item)
    cursor.execute(sql, x)

# SOMA

def soma(id_venda):
    
    sql = "SELECT SUM(valor) FROM item_venda WHERE id_venda = %s"
    x = (id_venda,)
    cursor.execute(sql, x)
    
    soma = cursor.fetchone()

    sql = "UPDATE venda SET vl_total_venda = %s WHERE id_venda = %s"
    x = (soma[0], id_venda)
    cursor.execute(sql, x)

sql = "SELECT * FROM venda"
cursor.execute(sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)

sql = "SELECT * FROM venda"
cursor.execute(sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)

conn.close()
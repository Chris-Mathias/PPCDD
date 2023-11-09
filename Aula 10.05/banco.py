import mysql.connector

def getConexao():

    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1415",
        database = "estoque"
    )

    return con


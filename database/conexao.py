import mysql.connector

def criar_conexao():
    conexao = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="root",
                                        database="produto"
    )
    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor
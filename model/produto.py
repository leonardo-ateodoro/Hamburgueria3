from database.conexao import criar_conexao

def recuperar_produtos():
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    select codigo,
                        produto,
                        descricao,
                        destaque,
                        preco,
                        url_imagem,
                        disponibilidade
                    from itens;
                   """)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def rec_destq():
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    SELECT codigo, 
                        url_imagem
                    from itens
                    WHERE destaque = 1;

    """)
    
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def recuperar_produto(codigo:int):
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    select codigo,
                           produto, 
                           descricao,
                           destaque,
                           preco,
                           url_imagem, 
                           disponibilidade 
                    from itens
                    where codigo = %s;
                   """, [codigo])
    produto = cursor.fetchone()
    conexao.close()
    return produto


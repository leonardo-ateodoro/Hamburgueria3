from database.conexao import criar_conexao

def recuperar_carrinho(usuario:str)->list:
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    SELECT  carrinhos.cod_carrinho,
                            carrinhos.usuario,
                            carrinhos.data,
                            carrinhos.finalizado,
                            itens.produto,
                            itens_carrinho.quantidade,
                            itens.preco,
                            itens.url_imagem 
                    FROM carrinhos
                    INNER JOIN itens_carrinho ON carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
                    INNER JOIN itens ON itens.codigo = itens_carrinho.cod_produto
                    WHERE carrinhos.usuario = %s;
                   """,[usuario])
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def inserir_item(usuario,cod_produto,quantidade=1):
    conexao,cursor = criar_conexao()
    cursor.execute("""
                   select cod_carrinho from carrinhos
                   where usuario = %s
                   and finalizado = 0
                   limit 1;
                   """, [usuario])
    resultado_carrinho = cursor.fetchone()
    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho ["cod_carrinho"]
    else:
        cursor.execute("""
                       INSERT INTO carrinhos (usuario)
                       VALUES  (%s, 0);
                       """, [usuario])
        codigo_carrinho = cursor.lastrowid

    cursor.execute("""
                       INSERT INTO itens_carrinho
                       (cod_carrinho, cod_produto)
                       VALUES
                       (%s, %s, %s);
                       """[codigo_carrinho, cod_produto, quantidade])
    conexao.commit()
    conexao.close()

    

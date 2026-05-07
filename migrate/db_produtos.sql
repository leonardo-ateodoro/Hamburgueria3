create database if not exists produto;
use produto;

CREATE table IF NOT EXISTS itens(
	codigo int NOT NULL PRIMARY KEY auto_increment,
	produto varchar(50),
	descricao varchar(50),
	destaque bool,
	preco float,
	url_imagem varchar(300),
	disponibilidade bool default 1
);

CREATE TABLE IF NOT EXISTS usuarios(
	usuario varchar(20) PRIMARY KEY,
    senha varchar(200) NOT NULL,
    nome varchar(100) DEFAULT "ANONIMO"
);

CREATE TABLE IF NOT EXISTS carrinhos(
	cod_carrinho int auto_increment primary key,
    usuario varchar(20),
    data datetime default CURRENT_TIMESTAMP,
    finalizado bool,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
    );


CREATE TABLE IF NOT EXISTS itens_carrinho(
	cod_item_carrinho int auto_increment primary key,
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    CONSTRAINT fk_itenscarrinho_carrinhos FOREIGN KEY (cod_carrinho) REFERENCES carrinhos(cod_carrinho),
    CONSTRAINT fk_itenscarrinho_itens FOREIGN KEY (cod_produto) REFERENCES itens(codigo)
)
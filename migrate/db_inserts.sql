USE produto;
INSERT INTO `produto`.`itens`
(
produto, 
descricao, 
destaque, 
preco, 
url_imagem, 
disponibilidade
)
VALUES(
"X-TUDO",
"Compra que é top",
"1",
"40.00",
"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200",
"1"
),

("X-TO",
"Compra que é top",
"0",
"40.00",
"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200",
"1"
),

("X-SALADA",
"Compra que é top",
"1",
"40.00",
"https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=200",
"1"
);

INSERT INTO `produto`.`usuarios` (`usuario`, `senha`, `nome`) VALUES ('Godofredo', '123', 'Godofredo Frederico');
INSERT INTO `produto`.`usuarios` (`usuario`, `senha`, `nome`) VALUES ('Felizberta', 'fefe', 'Felizberta Feliz');

INSERT INTO `produto`.`carrinhos` (`usuario`, `finalizado`) VALUES ('Godofredo', '0');

INSERT INTO `produto`.`itens_carrinho` (`cod_carrinho`, `cod_produto`, `quantidade`) VALUES ('1', '2', '2');
INSERT INTO `produto`.`itens_carrinho` (`cod_carrinho`, `cod_produto`, `quantidade`) VALUES ('1', '1', '3');
INSERT INTO `produto`.`itens_carrinho` (`cod_carrinho`, `cod_produto`, `quantidade`) VALUES ('1', '3', '1');



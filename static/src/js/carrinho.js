async function mostrarCarrinho()
{
    const resposta = await fetch('http://10.110.134.2:8080/api/get/carrinho');
    const dados = await resposta.json();

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{


        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";

        let total = 0;

        for (let dado of dados){

            total = total + dado.preco

            let linha = `
                        teste
                        <img src="${dado.imagem}" alt="Hambúrguer" class="cart-item__image">

                        <div class="cart-item__info">
                            
                            <!-- TOPO (nome + remover) -->
                            <div class="cart-item__top">
                                <h3 class="cart-item__name">${dado.nome}</h3>
                                <button class="remove-item-btn" title="Remover item">🗑️</button>
                            </div>

                            <!-- PARTE DE BAIXO -->
                            <div class="cart-item__bottom">
                                <span class="cart-item__price">R$ ${dado.preco}</span>
                            </div>
                        </div>
                        `
            carrinho.innerHTML += linha

        }
        document.querySelector(".cart-item__price").textContent = "R$ " + total

    }
}

mostrarCarrinho();

async function inserirItemCarrinho (cod_produto, quantidade=1) {
     const resposta = await fetch ( "/api/post/item_carrinho", 
                                    {
                                    method: "POST",
                                    headers:{
                                        "Content-Type":"application/json"
                                    },
                                    body: JSON.stringify(
                                        {
                                            "cod_produto": cod_produto,
                                            "quantidade": quantidade
                                        }
                                    )
                                                                           {
                                        
                                    
                                    }

     )

     if (!resposta.ok)
        
        alert ("Erro ao inserir item!")
}
mostrarCarrinho();\

}
    

from flask import Flask, jsonify, redirect, render_template, request, session
from model.carrinho import recuperar_carrinho, inserir_item
from model.produto import recuperar_produtos, rec_destq, recuperar_produto
from model.usuario import Usuario

app = Flask(__name__)

app.secret_key = "banana_verde"

@app.route("/")
def pagina_inicial():
    produtos = recuperar_produtos()
    destaques = rec_destq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto/<codigo>")
def pagina_pagina2(codigo):
    produto = recuperar_produto(codigo)
    return render_template("produto.html", produto =produto)

@app.route("/logar")
def logar():
    session["nome"] = "Godofredo"
    return redirect("/")

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usuario = Usuario(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")

@app.route("/logar/usuario", methods=["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = Usuario.logar(usuario, senha)

    if not resultado:
        session["usuario_logado"] = resultado
    
    return redirect("/")

@app.route("/api/get/carrinho", methods = ["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
        login = (session["usuario_logado"]["login"])
        carrinho = recuperar_carrinho(login)
        return jsonify(carrinho), 200
    else:
        return jsonify({"message": "Usuário não logado"}), 401
    
@app.route("/cadastro_login")
def cadastro_login():
    return render_template("cadastro_login.html")


app.run(debug=True)

@app.route("/api/post/item_carrinho", methods = ["POST"])
def api_post_item_carrinho():
    if "usuario_logado " in session:
        usuario = session ["usuario_logado"]["usuario"]
        dados_json = request.get_json()
        codigo_produto = dados_json.get("cod_produto")
        quantidade = dados_json.get("quantidade")
        inserir_item(usuario, codigo_produto, quantidade)
        return jsonify({"message": "Inserido com sucesso"}), 201
    else:
        return redirect ("/login")


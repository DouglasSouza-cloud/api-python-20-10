# Desenvolver um back end com API
# Postman - teste http -> verificar respostas da API
#1. OBJETIVO
#2. URLBASE
#3. ENDPOINTS
#4. RECURSOS DISPONIBILIZADOS

# VAMOS CRIAR UMA API

"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR

C.R.U.D
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
#APP -> REPRESENTA A APLICAÇÃO FLASK
#__NAME__ -> IDENTIFICA O MÓDULO DA APLICAÇÃO

livros = [
    {
        "id": 1,
        "titulo": "O Espetacular Homem-Aranha: Edição Definitiva",
        "autor": "Stan Lee e Steve Ditko",
    },

    {
        "id": 2,
            "titulo": "Homem Aranha: Historia de Vida",
            "autor": "Chip Zdarsky e Mark Bagley",
    },

    {
        "id": 3,
            "titulo": "Homem-Aranha: De Volta ao Lar",
            "autor": "Stan Lee e Steve Ditko",
    }
]

#CONSULTAR LIVROS - CRIAR UMA FUNÇÃO

def obter_livros():
    return jsonify(livros)

#CRIAR AS ROTAS /LIVROS
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

#INICIALIZAÇÃO DO SERVIDOR LOCAL
app.run(host="localhost",
        port=5000, 
        debug=True
        )

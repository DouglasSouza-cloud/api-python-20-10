from flask import Flask, jsonify, request
from flask_babel import Babel, _
app = Flask(__name__)

# CONFIGURACOES DE IDIOMA
app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'America/Sao_Paulo'

# PERMITE EXIBIR ACENTOS NAS RESPOSTAS JSON
app.json.ensure_ascii = False

# SELECIONA O IDIOMA
def get_locale():
    return request.accept_languages.best_match(['pt_BR', 'en']) or 'pt_BR'

# INICIALIZA O FLASK-BABEL
babel = Babel(app, locale_selector=get_locale)

# LISTA DE LIVROS
livros = [
    {
        "id": 1,
        "titulo": "Homem-Aranha: A Última Caçada de Kraven",
        "autor": "J.M. DeMatteis e Mike Zeck",
    },
    {
        "id": 2,
        "titulo": "Homem-Aranha: Azul",
        "autor": "Jeph Loeb e Tim Sale",
    },
    {
        "id": 3,
        "titulo": "Homem-Aranha: Amigão da Vizinhança",
        "autor": "Tom Taylor e Juannal Frigeri",
    },
    {
        "id": 4,
        "titulo": "Homem-Aranha: Universo Aranha",
        "autor": "Dan Slott e Olivier Coipel",
    },
    {
        "id": 5,
        "titulo": "Bleach: Vol. 1 - O Substituto de Ceifador de Almas",
        "autor": "Tite Kubo",
    },
    {
        "id": 6,
        "titulo": "Hunter x Hunter: Vol. 1 - O Dia da Partida",
        "autor": "Yoshihiro Togashi",
    },
        {
        "id": 7,
        "titulo": "One Piece: Vol. 1 - Romance Dawn",
        "autor": "Eiichiro Oda",
    },
    {
        "id": 8,
        "titulo": "Bleach: Can't Fear Your Own World (Light Novel)",
        "autor": "Ryohgo Narita e Tite Kubo",
    },
    {
        "id": 9,
        "titulo": "One Piece: Ace's Story (Light Novel)",
        "autor": "Sho Hinata e Eiichiro Oda",
    },
    {
        "id": 10,
        "titulo": "Hunter x Hunter: O Exame Hunter",
        "autor": "Yoshihiro Togashi",
    }
]

# CONSULTAR LIVROS
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

# CRIAR AS ROTAS /LIVROSid
@app.route("/livros/<int:id>",methods=["GET"])

# <int:> -> indica que determinada variavel é inteiro
def obter_livros_por_id(id):
    for livro in livros: 
        if livro.get("id") == id:
            return jsonify(livro)
        else:
            return jsonify ({"message":"LIVRO NÃO ENCONTRADO!"}), 404
        
# PUT -> primeiro, os dados enviados pelo cliente serão obtidos
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):

    # permite acessar os dados json enviados no corpo da requisição(body)
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id")== id:
            livros[indice].update(livro_alterado)
            return jsonify(livros)
        
# CRIAÇÃO DE UM NOVO LIVRO 
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# INICIALIZACAO DO SERVIDOR LOCAL
if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):

    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)
<div align="center">

# 📚 API de Livros — Flask

**Uma API REST para consultar, cadastrar, editar e excluir livros usando Python e Flask.**

<br>

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-6DB33F?style=for-the-badge)
![Status](https://img.shields.io/badge/status-projeto%20de%20estudo-blueviolet?style=for-the-badge)

</div>

---

## 🚀 Sobre o projeto

Este projeto consiste em uma **API REST desenvolvida em Python com Flask**, criada para praticar os fundamentos da construção de serviços web e o gerenciamento de dados por meio de requisições HTTP.

A aplicação disponibiliza uma coleção de livros — incluindo quadrinhos, mangás e light novels — e permite realizar operações básicas de **CRUD** (*Create, Read, Update e Delete*).

Os dados são mantidos em uma lista na memória da aplicação. Por isso, as alterações não são persistidas em um banco de dados e podem ser perdidas quando o servidor é reiniciado.

## ✨ Funcionalidades

| Método | Endpoint | Função |
|:---:|---|---|
| `GET` | `/livros` | Retorna a lista de livros cadastrados |
| `GET` | `/livros/<id>` | Consulta um livro pelo identificador |
| `POST` | `/livros` | Adiciona um novo livro |
| `PUT` | `/livros/<id>` | Atualiza os dados de um livro |
| `DELETE` | `/livros/<id>` | Remove um livro da coleção |

## 🧰 Tecnologias utilizadas

- **[Python](https://www.python.org/)** — linguagem de programação.
- **[Flask](https://flask.palletsprojects.com/)** — criação da aplicação web e definição das rotas.
- **Flask-Babel** — configuração de idioma conforme o cabeçalho `Accept-Language` da requisição.
- **JSON** — formato utilizado para receber e devolver os dados da API.
- **HTTP** — métodos e códigos de resposta para comunicação entre cliente e servidor.

## 📁 Estrutura do projeto

```text
api-python-20-10/
├── app.py              # Aplicação Flask, dados e endpoints da API
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

> A pasta `.venv/` é o ambiente virtual local. Ela não precisa ser enviada ao repositório; cada pessoa pode criar seu próprio ambiente a partir das dependências.

## ⚙️ Como executar

### 1. Pré-requisitos

- Python instalado.
- Git (opcional, para clonar o repositório).
- Um terminal, como o PowerShell ou o terminal integrado do VS Code.

Confira se o Python está disponível:

```bash
python --version
```

### 2. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd api-python-20-10
```

Se você já baixou o projeto, entre diretamente na pasta dele.

### 3. Crie um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (Prompt de Comando):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Inicie a API

```bash
python app.py
```

Com o servidor em execução, a API estará disponível em:

**http://localhost:5000**

Para interromper o servidor, use `Ctrl + C` no terminal.

## 🔎 Testando os endpoints

Você pode testar as rotas usando o navegador para requisições `GET` ou ferramentas como **Postman**, **Insomnia** e `curl` para enviar outros métodos HTTP.

### Listar todos os livros

```http
GET http://localhost:5000/livros
```

Exemplo de resposta:

```json
[
  {
    "id": 1,
    "titulo": "Homem-Aranha: A Última Caçada de Kraven",
    "autor": "J.M. DeMatteis e Mike Zeck"
  }
]
```

### Buscar um livro pelo ID

```http
GET http://localhost:5000/livros/1
```

### Cadastrar um livro

```http
POST http://localhost:5000/livros
Content-Type: application/json
```

Corpo da requisição:

```json
{
  "id": 11,
  "titulo": "Título do livro",
  "autor": "Nome do autor"
}
```

### Editar um livro

```http
PUT http://localhost:5000/livros/1
Content-Type: application/json
```

Corpo da requisição:

```json
{
  "titulo": "Novo título",
  "autor": "Novo autor"
}
```

### Excluir um livro

```http
DELETE http://localhost:5000/livros/1
```

## 🌐 Idioma das respostas

A aplicação utiliza o **Flask-Babel** para selecionar o idioma com base no cabeçalho `Accept-Language`. O idioma padrão está configurado como português do Brasil (`pt_BR`), com inglês (`en`) como alternativa.

Exemplo de cabeçalho:

```http
Accept-Language: en
```

> A seleção de idioma está configurada no projeto, mas as mensagens das rotas ainda não estão todas internacionalizadas com `_()`.

## 🧠 Conceitos praticados

- Criação de rotas com Flask.
- Uso dos métodos HTTP `GET`, `POST`, `PUT` e `DELETE`.
- Recebimento de dados JSON com `request.get_json()`.
- Retorno de respostas JSON com `jsonify()`.
- Parâmetros dinâmicos de rota, como `<int:id>`.
- Manipulação de listas e dicionários em Python.
- Organização de dependências com `requirements.txt`.
- Configuração básica de internacionalização com Flask-Babel.

## ⚠️ Limitações conhecidas

Este projeto tem finalidade educacional e pode ser aprimorado. Na versão atual:

- Os dados ficam apenas na memória, sem persistência em banco de dados.
- A validação dos dados enviados pelo cliente é limitada.
- Algumas rotas não retornam uma resposta específica quando o ID não existe.
- A API ainda não possui autenticação, testes automatizados ou documentação OpenAPI.
- O servidor está configurado para execução local com `debug=True`; essa configuração não deve ser usada em produção.

## 🛣️ Próximas melhorias

- [ ] Validar os campos obrigatórios e o formato do JSON.
- [ ] Padronizar as respostas de erro e os códigos HTTP.
- [ ] Corrigir e testar todos os cenários de consulta, edição e exclusão.
- [ ] Adicionar testes automatizados com `pytest`.
- [ ] Implementar persistência com SQLite ou MySQL.
- [ ] Completar a internacionalização das mensagens.
- [ ] Documentar a API com Swagger/OpenAPI.
- [ ] Preparar uma configuração segura para produção.

## 👨‍💻 Objetivo

Projeto desenvolvido para fins de **aprendizado de Python, desenvolvimento web e construção de APIs REST**.

---

<div align="center">

Feito com 🐍 Python + ⚗️ Flask

</div>

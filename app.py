# Do módulo flask (MINUSCULO), Importa a classe Flask (MAIUSCULO) from flask import Flask
# app se chama app pq é uma convenção
# que argumento eu passo pro flask? O nome da aplicação app = Flask("hello")
# ##estou criando minha primeira rota @app.route("/")
# ##CRIA UMA FUNÇÃO QUE RETORNA HELLO WORLD def hello(): return "Hello World" 
from flask import Flask, render_template
from datetime import datetime

app = Flask("Ola")

posts = [
    {
        "title": "O meu primeiro post.",
        "body": "Aqui é o texto do post.",
        "author": "Rodrigo",
        "created": datetime(2022,7,25)
    },
    {
        "title": "O meu segundo post.",
        "body": "Aqui é o texto do post.",
        "author": "Sara",
        "created": datetime(2022,7,26)
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)
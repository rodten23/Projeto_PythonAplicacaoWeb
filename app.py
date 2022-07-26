# Do módulo flask (MINUSCULO), Importa a classe Flask (MAIUSCULO) from flask import Flask
# app se chama app pq é uma convenção
# que argumento eu passo pro flask? O nome da aplicação app = Flask("hello")
# ##estou criando minha primeira rota @app.route("/")
# ##CRIA UMA FUNÇÃO QUE RETORNA HELLO WORLD def hello(): return "Hello World" 
from flask import Flask, render_template

app = Flask("Ola")

@app.route("/")
@app.route("/ola")
def ola():
    return "Olá, Mundo!"

@app.route("/contato")
def contato():
    return render_template("/index.html")
    
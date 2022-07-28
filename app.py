# Do módulo flask (MINUSCULO), Importa a classe Flask (MAIUSCULO) from flask import Flask
# app se chama app pq é uma convenção
# que argumento eu passo pro flask? O nome da aplicação app = Flask("hello")
# ##estou criando minha primeira rota @app.route("/")
# ##CRIA UMA FUNÇÃO QUE RETORNA HELLO WORLD def hello(): return "Hello World" 
from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("Ola")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author')


db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    user = User(username='rodrigo', email='r@t.com.br', password_hash='rat')
    post1 = Post(title="Post 1", body="Texto do Post AA", author=user)
    post2 = Post(title="Post 2", body="Texto do Post BB", author=user)
    db.session.add(user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect(url_for('index'))
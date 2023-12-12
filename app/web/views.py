from app.web import web_bp as app
from flask import render_template,url_for
from . import web_bp

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login')
def login_front():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")
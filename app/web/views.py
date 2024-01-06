from app.web import web_bp as app
from flask import render_template, url_for, jsonify
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

@app.route('/teacher')
def teacher():
    return render_template("teacher.html")

@app.route('/personinfo')
def personinfo():
    return render_template('personinfo.html')

@app.route('/courseinfo')
def courseinfo():
    return render_template('courseinfo.html')

@app.route('/scinfo')
def scinfo():
    return render_template('scinfo.html')
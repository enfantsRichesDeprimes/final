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


@app.route('/createcourse')
def createcourse():
    return render_template("createcourse.html")


@app.route('/alluser')
def alluser():
    return render_template("alluser.html")


@app.route('/allcourse')
def allcourse():
    return render_template("allcourse.html")


@app.route('/searchcourse')
def searchcourse():
    return render_template("searchcourse.html")


@app.route('/searchuser')
def searchuser():
    return render_template("searchuser.html")

@app.route('/searchsc')
def searchsc():
    return render_template("searchsc.html")
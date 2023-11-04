from app import app, render_template, flash, request, db, redirect, url_for
from ...models.ocorrencias import Ocorrencias



@app.route("/historico")
def historico():
    return render_template("relatorios/historico.html")


@app.route("/ocorrencias")
def ocorrencias():
    return render_template("relatorios/ocorrencias.html")


@app.route("/homepage")
def homepage():
    return render_template("home/homepage.html")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.Services.tabela_teste import select_all_tabela_teste, add_teste
app = Flask(__name__)


@app.route("/")
def princial_page():
    return dict(
        Description="",
        Author="Gabriel Nantes",
        GitHub="https://github.com/gabrielnantes/"
    )


@app.route("/select-all")
def select_all():
    return select_all_tabela_teste()


@app.route("/insere-tb-teste", methods=["POST"])
def insere_tb_teste():
    return add_teste()


app.run(debug=True)

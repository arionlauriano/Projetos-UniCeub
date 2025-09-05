from flask import Blueprint, render_template, request
from dao.Autores_dao import Autores, AutoresDAO

bp_aut = Blueprint("aut", __name__)

@bp_aut.route("/form_create")
def form_create():
    return render_template("aut/form_create.html", msg="", display="none")

@bp_aut.route("/create", methods=["POST"])
def create():
    a = Autores()
    a.nome_autor = request.form["nome_autor"]

    a_dao = AutoresDAO()
    a_dao.inserir_autores(a)
    if a.cod_autor is None:
        msg = "Erro ao inserir autor."
    else:
        msg = f"Autor número {a.cod_autor} inserido."
    return render_template("/aut/form_create.html", msg=msg, display="block")


@bp_aut.route("/read")
def read():
    aut_dao = AutoresDAO()
    lst = aut_dao.select_alfabetico()
    if not lst:
       msg = "Não há autores na database."
    else:
       msg = f"{len(lst)} autores listados na database."
    return render_template("/aut/read.html")
from flask import Blueprint, render_template, request
from Aula03a07.dao.Autores_dao import Autores, AutoresDAO

bp_aut = Blueprint("aut", __name__)

@bp_aut.route("/form_create")
def form_create():
    return render_template("/aut/form_crate.html", msg="", display="none")

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
    return render_template("/aut/form_crate.html", msg=msg, display="block")

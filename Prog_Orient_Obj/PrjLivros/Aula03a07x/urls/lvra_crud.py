from flask import Blueprint, render_template, request
from Aula03a07.dao.livros_adiquiridos_dao import Livros_Ad, Livros_AdDAO
from Aula03a07.dao.Autores_dao import AutoresDAO

bp_lvra = Blueprint("lrva", __name__)

@bp_lvra.route("/form_create")
def form_create():
    dao = AutoresDAO
    lst = dao.select_alfabetico()
    return render_template("/lvra/form_create.html", msg="", display="none", lst=lst)

@bp_lvra.route("/create", methods=["POST"])
def create():
    la=Livros_Ad()
    la.nome_livro = request.form["nome_livro"]
    la.id_autor = request.form["id_autor"]

    ladao= Livros_AdDAO
    ladao.inserir_livros(la)
    if la.cod_livro is None:
        msg = "Erro ao inserir modelo."
    else:
        msg = f"Modelo número {la.cod_livro} inserido."
        return render_template("/lvra/form_create.html", msg=msg, display="block", lst=lst)
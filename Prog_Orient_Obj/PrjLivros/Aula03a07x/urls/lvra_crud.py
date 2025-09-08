from flask import Blueprint, render_template, request
from dao.livros_adiquiridos_dao import Livros_Ad, Livros_AdDAO
from dao.Autores_dao import AutoresDAO

bp_lvra = Blueprint("lvra", __name__)

@bp_lvra.route("/form_create")
def form_create():
    return render_template("lvra/form_create.html", msg="", display="none")

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
        return render_template("/lvra/form_create.html", msg=msg, display="block")
    
@bp_lvra.route("/read")
def read():
    la_dao = Livros_AdDAO()
    lstLA = la_dao.selecionar()
    if not lstLA:
        msg = "Não há livros na database."
    else:
       msg = f"{len(lstLA)} livros listados na database."
    return render_template("/lvra/read.html", msg=msg, lstLA=lstLA)
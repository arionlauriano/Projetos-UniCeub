from flask import Blueprint, render_template, request
from dao.livros_adiquiridos_dao import Livros_Ad, Livros_AdDAO
from dao.Autores_dao import AutoresDAO

bp_lvra = Blueprint("lvra", __name__)

@bp_lvra.route("/form_create")
def form_create():
    aut_dao = AutoresDAO()
    lstAut = aut_dao.select_alfabetico()
    return render_template("lvra/form_create.html", msg="", display="none", lstAut=lstAut)

@bp_lvra.route("/create", methods=["POST"])
def create():
    la=Livros_Ad()
    la.nome_livro = request.form["nome_livro"]
    la.id_autor = request.form["id_autor"]

    ladao= Livros_AdDAO()
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


@bp_lvra.route("/edit")
def edit():
    la_dao = Livros_AdDAO()
    lstLA = la_dao.selecionar()

    if not lstLA:
        msg = "Não há livros na database."
    else:
        msg = f"{len(lstLA)} livros registrados na database."
    return render_template("/lvra/edit.html", lstLA=lstLA, msg=msg)

@bp_lvra.route("/delete/<int:cod>")
def delet(cod):
    la_dao = Livros_AdDAO()
    if la_dao.deletar_livros(cod):
        msg = "Livro deletado da database."
    else:
        msg = "Erro ao deletar livro da database."
    lstLA = la_dao.selecionar()
    if not lstLA:
        msg += " | Não há livros na database."
    else:
        msg += f" | {len(lstLA)} livros listados na database."
    return render_template("/lvra/edit.html", lstLA=lstLA, msg=msg)

@bp_lvra.route("form_update/<int:idt>")
def form_update(idt):
    lvra_dao = Livros_AdDAO()
    lvra=lvra_dao.consulta_id(idt)
    aut_dao = AutoresDAO()
    lst_aut = aut_dao.select_alfabetico()
    return render_template("lvra/form_update.html", lvra=lvra, msg="", display="none", lst_aut=lst_aut)

@bp_lvra.route("/save_update", methods=["POST"])
def save_update():
    lvra = Livros_Ad()
    lvra.cod_livro = request.form["cod_livro"]
    lvra.nome_livro = request.form["nome_livro"]
    lvra.id_autor = request.form["id_autor"]

    aut_dao = AutoresDAO()
    lst_aut = aut_dao.select_alfabetico()

    lvra_dao = Livros_AdDAO()
    lvra_dao.atualizar_livros(lvra)
    msg = f"Livro número {lvra.cod_livro} alterado."
    return render_template("/lvra/form_update.html", lvra=lvra, msg=msg, lst_aut=lst_aut, display="block")
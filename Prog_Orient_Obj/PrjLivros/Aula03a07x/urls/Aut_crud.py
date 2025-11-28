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
    return render_template("/aut/read.html", msg=msg, lst=lst)

@bp_aut.route("/edit")
def edit():
    aut_dao = AutoresDAO()
    lst_aut = aut_dao.select_alfabetico()
    if not lst_aut:
        msg = "Não há autores na database."
    else:
        msg = f"{len(lst_aut)} autores na database."
    return render_template("/aut/edit.html", msg=msg, lst_aut=lst_aut)

@bp_aut.route("/delete/<int:cod>")
def delete(cod):
    aut_dao = AutoresDAO()
    if aut_dao.deletar(cod):
        msg = "Autor excluido da database."
    else:
        msg = "Erro ao excluir autor. Confira se há livros associados."
    lst_aut = aut_dao.select_alfabetico()
    if not lst_aut:
        msg += "| Não há autores na database."
    else:
        msg += f"| {len(lst_aut)} autores listados na database."
    return render_template("/aut/edit.html", msg=msg, lst_aut=lst_aut)

@bp_aut.route("form_update/<int:idt>")
def form_update(idt):
    aut_dao = AutoresDAO()
    autor = aut_dao.consulta_por_id(idt)
    return render_template("aut/form_update.html", aut=autor, msg="", display="none")

@bp_aut.route("/save_update", methods=["POST"])
def save_update():
    aut = Autores()
    aut.cod_autor = request.form["cod_autor"]
    aut.nome_autor = request.form["nome_autor"]
    
    aut_dao = AutoresDAO()
    aut_dao.atualizar(aut)

    msg = f"Autor, {aut.cod_autor} alterada com sucesso."

    return render_template("/aut/form_update.html", aut=aut, msg=msg, display="block")
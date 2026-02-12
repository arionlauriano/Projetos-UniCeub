from flask import Blueprint, render_template, request
from dao.mont_dao import Montadora, MontadoraDao


bp_mont = Blueprint("mont", __name__)

@bp_mont.route("/mont_form_create")
def mont_form_create():
    return render_template("mont/mont_form_create.html", msg="", display="none")

@bp_mont.route("/mont_create", methods=["POST"])
def mont_create():
    mont = Montadora()
    mont.sgl_mont = request.form["sgl_mont"]
    mont.nome_mont = request.form["nome_mont"]

    mont_dao = MontadoraDao()
    mont_dao.add_mont(mont)
    if mont.id_mont is None:
        msg = "Erro ao inserir montadora."
    else:
        msg = f"Montadora, {mont.sgl_mont} - {mont.nome_mont}, adicionada."
    return render_template("/mont/mont_form_create.html", msg=msg, display="block")

@bp_mont.route("/mont_read")
def mont_read():
    mont_dao = MontadoraDao()
    lst = mont_dao.select_mont_az()
    if not lst:
        msg = "Não há montadoras da database."
    else:
        msg = f"{len(lst)} montadoras listadas na database."
    return render_template("/mont/mont_read.html", msg=msg, lst=lst)

@bp_mont.route("/mont_edit")
def mont_edit():
    mont_dao = MontadoraDao()
    lst = mont_dao.select_mont_az()
    if not lst:
        msg = "Não há montadoras na database"
    else:
        msg = f"{len(lst)} montadoras listadas na database"
    return render_template("/mont/mont_edit.html", msg=msg, lst=lst)

@bp_mont.route("/mont_dell/<int:cod>")
def mont_dell(cod):
    mont_dao = MontadoraDao()
    mont_dao.dell_mont(cod)
    if not mont_dao.select_mont_id(cod):
        msg = "Montadora excluída da database."
    else:
        msg = "Erro ao excluir montadora. Confira se há modelos associados."
    lst = mont_dao.select_mont_az()
    if not lst:
        msg += " | Não há montadoras na database."
    else:
        msg += f" | {len(lst)} montadoras listadas na database."
    return render_template("/mont/mont_edit.html", msg=msg, lst=lst)

@bp_mont.route("/mont_update/<int:cod>")
def mont_form_update(cod):
    mont_dao=MontadoraDao()
    mont = mont_dao.select_mont_id(cod)
    return render_template("/mont/mont_update.html", mont=mont, msg="", display="none")

@bp_mont.route("/mont_save_update", methods=["POST"])
def mont_save_update():
    mont = Montadora()
    mont.id_mont=request.form["id_mont"]
    mont.sgl_mont=request.form["sgl_mont"]
    mont.nome_mont=request.form["nome_mont"]
    
    mont_dao = MontadoraDao()
    mont_dao.update_mont(mont)

    msg= f"Montadora, {mont.sgl_mont} - {mont.nome_mont}, atualizada."

    return render_template("/mont/mont_update.html", mont=mont, msg=msg, display="block")
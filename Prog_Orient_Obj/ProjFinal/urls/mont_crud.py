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
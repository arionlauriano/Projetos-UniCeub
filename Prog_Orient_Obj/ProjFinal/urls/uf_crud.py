from flask import Blueprint, render_template, request
from dao.uf_dao import UF, UFdao

bp_uf = Blueprint("uf", __name__)


@bp_uf.route("/uf_form_create")
def uf_form_create():
    return render_template("uf/uf_form_create.html", msg="", display="none")


@bp_uf.route("/uf_create", methods=["POST"])
def uf_create():
    uf = UF()
    uf.sgl_uf = request.form["sgl_uf"]
    uf.nome_uf = request.form["nome_uf"]

    uf_dao = UFdao()
    uf_dao.add_uf(uf)

    if uf.id_uf is None:
        msg = "Erro ao inserir UF."
    else:
        msg = f"UF {uf.sgl_uf} - {uf.nome_uf} adicionada com sucesso."

    return render_template("uf/uf_form_create.html", msg=msg, display="block")


@bp_uf.route("/uf_read")
def uf_read():
    uf_dao = UFdao()
    lst = uf_dao.select_uf_az()

    if not lst:
        msg = "Não há UFs cadastradas."
    else:
        msg = f"{len(lst)} UFs encontradas."

    return render_template("uf/uf_read.html", msg=msg, lst=lst)


@bp_uf.route("/uf_edit")
def uf_edit():
    uf_dao = UFdao()
    lst = uf_dao.select_uf_az()

    if not lst:
        msg = "Não há UFs na database."
    else:
        msg = f"{len(lst)} UFs listadas na database."

    return render_template("uf/uf_edit.html", msg=msg, lst=lst)


@bp_uf.route("/uf_dell/<int:cod>")
def uf_delete(cod):
    uf_dao = UFdao()
    uf_dao.dell_uf(cod)

    if not uf_dao.select_uf_id(cod):
        msg = "UF excluída com sucesso."
    else:
        msg = "Erro ao excluir UF."

    lst = uf_dao.select_uf_az()

    if not lst:
        msg += " | Não há UFs na database."
    else:
        msg += f" | {len(lst)} UFs listadas."

    return render_template("uf/uf_edit.html", msg=msg, lst=lst)


@bp_uf.route("/uf_update/<int:cod>")
def uf_form_update(cod):
    uf_dao = UFdao()
    uf = uf_dao.select_uf_id(cod)
    return render_template("uf/uf_update.html", uf=uf, msg="", display="none")


@bp_uf.route("/uf_save_update", methods=["POST"])
def uf_save_update():
    uf = UF()
    uf.id_uf = request.form["id_uf"]
    uf.sgl_uf = request.form["sgl_uf"]
    uf.nome_uf = request.form["nome_uf"]

    uf_dao = UFdao()
    uf_dao.update_uf(uf)

    msg = f"UF {uf.sgl_uf} - {uf.nome_uf} atualizada com sucesso."

    return render_template("uf/uf_update.html", uf=uf, msg=msg, display="block")

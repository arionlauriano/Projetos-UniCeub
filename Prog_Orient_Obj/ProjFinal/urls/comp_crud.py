from flask import Blueprint, render_template, request
from dao.comp_dao import Compra, CompraDao
from dao.cli_dao import ClienteDao
from dao.vers_dao import VersaoDao

bp_comp = Blueprint("comp", __name__)

@bp_comp.route("comp_form_create")
def comp_form_create():
    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()

    return render_template("/comp/comp_form_create.html", msg="", display="none", lst_vers=lst_vers, lst_cli=lst_cli)

@bp_comp.route("/comp_create", methods=["POST"])
def comp_create():
    comp = Compra()
    comp.data_comp = request.form["data_comp"]
    comp.cod_nf_comp = request.form["cod_nf"]
    comp.total_comp = request.form["total_comp"]
    comp.cod_cli = request.form["cod_cli"]
    comp.cod_vers = request.form["cod_vers"]

    comp_dao = CompraDao()
    comp_dao.add_comp(comp)



    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()

    if not comp_dao.select_comp_id(comp.id_comp):
        msg = "Erro ao registrar compra."
    else:
        msg = f"Compra número {comp.id_comp} registrada."
    return render_template("/comp/comp_form_create.html", msg=msg, display="block", lst_cli=lst_cli, lst_vers=lst_vers)

@bp_comp.route("/comp_read")
def comp_read():
    comp_dao = CompraDao()
    lst = comp_dao.select_comp_az()

    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()

    if not lst:
        msg = "Não há compras registradas na database."
    else:
        msg = f"{len(lst)} compras registradas na database."
    return render_template("/comp/comp_read.html", msg=msg, lst=lst, lst_vers=lst_vers, lst_cli=lst_cli)

@bp_comp.route("/comp_read_vers", methods=["POST"])
def comp_read_vers():
    cod_vers = request.form["cod_vers"]

    comp_dao = CompraDao()
    lst = comp_dao.select_comp_vers_az(cod_vers)

    vers_dao = VersaoDao()
    vers = vers_dao.select_vers_id(cod_vers)
    if not lst:
        msg = f"Não há compras registradas para a versão, {vers.nome_vers}."
    else:
        msg = f"{len(lst)}, compras registradas para a versão, {vers.nome_vers}"
    return render_template("/comp/comp_read_vers.html", msg=msg, lst=lst, vers=vers)

@bp_comp.route("/comp_read_cli", methods=["POST"])
def comp_read_cli():
    cod_cli = request.form["cod_cli"]

    comp_dao = CompraDao()
    lst = comp_dao.select_comp_cli_az(cod_cli)

    cli_dao = ClienteDao()
    cli = cli_dao.select_cli_id(cod_cli)
    if not lst:
        msg = f"Não há compras registradas para o cliente, {cli.nome_cli}."
    else:
        msg = f"{len(lst)} compras registradas para o cliente, {cli.nome_cli}"
    return render_template("/comp/comp_read_cli.html", msg=msg, lst=lst, cli=cli)

@bp_comp.route("/comp_edit")
def comp_edit():
    comp_dao = CompraDao()
    lst = comp_dao.select_comp_az()

    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()
    if not lst:
        msg = "Não há compras registradas na database."
    else:
        msg = f"{len(lst)} compras registradas na database."
    return render_template("/comp/comp_edit.html", lst=lst, lst_cli=lst_cli, lst_vers=lst_vers, msg=msg)

@bp_comp.route("/comp_edit_vers", methods=["POST"])
def comp_edit_vers():
    cod_vers = request.form["cod_vers"]

    comp_dao = CompraDao()
    lst = comp_dao.select_comp_vers_az(cod_vers)

    vers_dao = VersaoDao()
    vers = vers_dao.select_vers_id(cod_vers)
    if not lst:
        msg = f"Não há compras registradas para a versão, {vers.nome_vers}."
    else:
        msg = f"{len(lst)}, compras registradas para a versão, {vers.nome_vers}"
    return render_template("/comp/comp_edit_vers.html", msg=msg, lst=lst, vers=vers)

@bp_comp.route("/comp_edit_cli", methods=["POST"])
def comp_edit_cli():
    cod_cli = request.form["cod_cli"]

    comp_dao = CompraDao()
    lst = comp_dao.select_comp_cli_az(cod_cli)

    cli_dao = ClienteDao()
    cli = cli_dao.select_cli_id(cod_cli)
    if not lst:
        msg = f"Não há compras registradas para o cliente, {cli.nome_cli}."
    else:
        msg = f"{len(lst)} compras registradas para o cliente, {cli.nome_cli}"
    return render_template("/comp/comp_edit_cli.html", msg=msg, lst=lst, cli=cli)

@bp_comp.route("/comp_dell/<int:cod>")
def comp_dell(cod):
    comp_dao = CompraDao()
    comp_dao.dell_comp(cod)

    lst = comp_dao.select_comp_az()

    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()
    if not comp_dao.select_comp_id(cod):
        msg += " | Compra excluída da database."
    else:
        msg += " | Erro ao excluir copra."
    return render_template("/comp/comp_edit.html", msg=msg, lst=lst, lst_vers=lst_vers, lst_cli=lst_cli)

@bp_comp.route("/comp_update/<int:cod>")
def comp_form_update(cod):
    comp_dao = CompraDao()
    comp = comp_dao.select_comp_id(cod)

    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()
    return render_template("/comp/comp_update.html", comp=comp, msg="", display="none", lst_vers=lst_vers, lst_cli=lst_cli)

@bp_comp.route("/comp_save_update", methods=["POST"])
def comp_save_update():
    comp = Compra()
    comp.id_comp = request.form["id_comp"]
    comp.data_comp = request.form["data_comp"]
    comp.cod_nf_comp = request.form["cod_nf"]
    comp.total_comp = request.form["total_comp"]
    comp.cod_cli = request.form["cod_cli"]
    comp.cod_vers = request.form["cod_vers"]

    comp_dao = CompraDao()
    comp_dao.add_comp(comp)

    vers_dao = VersaoDao()
    lst_vers = vers_dao.select_vers_az()

    cli_dao = ClienteDao()
    lst_cli = cli_dao.select_cli_az()

    msg = f"Compra número {comp.id_comp}, atualizada."
    return render_template("/comp/comp_update.html", comp=comp, msg=msg, display="block", lst_cli=lst_cli, lst_vers=lst_vers)
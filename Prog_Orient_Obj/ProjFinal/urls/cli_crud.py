from flask import Blueprint, render_template, request
from dao.cli_dao import Cliente, ClienteDao
from dao.uf_dao import UFdao

bp_cli = Blueprint("cli", __name__)

@bp_cli.route("/cli_form_create")
def cli_form_create():
    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()
    return render_template("/cli/cli_form_create.html", msg="", display="none", lst_uf=lst_uf)

@bp_cli.route("/cli_create", methods=["POST"])
def cli_create():
    cli = Cliente()
    cli.nome_cli = request.form["nome_cli"]
    cli.data_nasc_cli = request.form["data_nasc_cli"]
    cli.cod_uf = request.form["cod_uf"]
    cli.cep_cli = request.form["cep_cli"]
    cli.end_cli = request.form["end_cli"]

    cli_dao = ClienteDao()
    cli_dao.add_cli(cli)

    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()
    if cli.id_cli is None:
        msg = "Erro ao inserir cliente."
    else:
        msg = f"Cliente, {cli.nome_cli}, adicionado."
    return render_template("/cli/cli_form_create.html", msg=msg, display="block", lst_uf=lst_uf)

@bp_cli.route("/cli_read")
def cli_read():
    cli_dao = ClienteDao()
    lst = cli_dao.select_cli_az()

    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()
    if not lst:
        msg = "Não há clientes na database."
    else:
        msg = f"{len(lst)} clientes listados na database."
    return render_template("/cli/cli_read.html", msg=msg, lst=lst, lst_uf=lst_uf)

@bp_cli.route("/cli_read_uf", methods=["POST"])
def cli_read_uf():
    cli_dao = ClienteDao()
    cod_uf = request.form["cod_uf"]
    lst = cli_dao.select_cli_uf_az(cod_uf)

    uf_dao = UFdao()
    uf = uf_dao.select_uf_id(cod_uf)
    if not lst:
        msg = "Não há clientes registrados nesse estado."
    else:
        msg = f"{len(lst)} clientes registrados no estado de {uf.nome_uf}"
    return render_template("/cli/cli_read_uf.html", msg=msg, lst=lst, uf=uf)

@bp_cli.route("/cli_edit")
def cli_edit():
    cli_dao = ClienteDao()
    lst = cli_dao.select_cli_az()

    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()

    if not lst:
        msg = "Não há clientes na database."
    else:
        msg = f"{len(lst)} clientes listados na database."
    return render_template("/cli/cli_edit.html", lst=lst, lst_uf=lst_uf, msg=msg)

@bp_cli.route("/cli_edit_uf", methods=["POST"])
def cli_edit_uf():
    cod_uf=request.form["cod_uf"]

    cli_dao=ClienteDao()
    lst = cli_dao.select_cli_uf_az(cod_uf)

    uf_dao=UFdao()
    uf = uf_dao.select_uf_id(cod_uf)
    if not lst:
        msg = "Não há clientes na database."
    else:
        msg = f"{len(lst)} registrados no estado de {uf.sgl_uf} - {uf.nome_uf}."
    return render_template("/cli/cli_edit_uf.html", msg=msg, lst=lst, uf=uf)

@bp_cli.route("/cli_dell/<int:cod>")
def cli_dell(cod):
    cli_dao = ClienteDao()
    cli_dao.dell_cli(cod)

    lst = cli_dao.select_cli_az()

    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()
    if not cli_dao.select_cli_id(cod):
        msg += " | Cliente excluído da database."
    else:
        msg += " | Erro ao excluir cliente. Confira se há compras associadas."
    return render_template("/cli/cli_edit.html", msg=msg, lst=lst, lst_uf=lst_uf)

@bp_cli.route("/cli_update/<id:cod>")
def cli_form_update(cod):
    cli_dao = ClienteDao()
    cli = cli_dao.select_cli_id(cod)

    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()    
    return render_template("/cli/cli_update.html", cli=cli, msg="", display="none", lst_uf=lst_uf)

@bp_cli.route("/cli_save_update", methods=["POST"])
def cli_save_update():
    cli = Cliente()
    cli.id_cli = request.form["id_cli"]
    cli.nome_cli = request.form["nome_cli"]
    cli.data_nasc_cli = request.form["data_nasc_cli"]
    cli.cod_uf = request.form["cod_uf"]
    cli.cep_cli = request.form["cep_cli"]
    cli.end_cli = request.form["end_cli"]

    cli_dao = ClienteDao()
    cli_dao.update_cli(cli)

    msg = f"Cliente, {cli.nome_cli}, atualizado."

    uf_dao = UFdao()
    lst_uf = uf_dao.select_uf_az()
    return render_template("/cli/cli_update.html", cli=cli, msg=msg, display="block", lst_uf=lst_uf)
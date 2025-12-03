from flask import Blueprint, render_template, request
from dao.vers_dao import Versao, VersaoDao
from dao.mod_dao import ModeloDao

bp_vers = Blueprint("vers", __name__)

@bp_vers.route("/vers_form_create")
def vers_form_create():
    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az
    return render_template("/vers/vers_form_create.html", msg="", display="none", lst_mod=lst_mod)

@bp_vers.route("/vers_create", methods=["POST"])
def vers_create():
    vers = Versao()
    vers.nome_vers = request.form["nome_vers"]
    vers.vlr_vers = request.form["vlr_vers"]
    vers.img_vers = request.form["img_vers"]
    vers.cod_mod = request.form["cod_mod"]

    vers_dao = VersaoDao()
    vers_dao.add_vers(vers)

    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az()
    if vers.id_vers is None:
        msg = "Erro ao inserir versão."
    else:
        msg = f"Versão, {vers.nome_vers}, adicionada."
    return render_template("/vers/vers_form_create.html", msg="", display="block", lst_mod=lst_mod)

@bp_vers.route("/vers_read")
def vers_read():
    vers_dao = VersaoDao()
    lst = vers_dao.select_vers_az()

    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az()
    if not lst:
        msg = "Não há versões na database."
    else:
        msg = f"{len(lst)} versões listadas na database."
    return render_template("/vers/vers_read.html", msg=msg, lst=lst, lst_mod=lst_mod)

@bp_vers.route("/vers_read_mod", methods=["POST"])
def vers_read_mod():
    cod_mod = request.form["cod_mod"]

    vers_dao = VersaoDao()
    lst = vers_dao.select_vers_mod_az(cod_mod)

    mod_dao = ModeloDao()
    mod = mod_dao.select_mod_id(cod_mod)
    if not lst:
        msg = f"Não há versões registradas para o modelo, {mod.nome_mod}."
    else:
        msg = f"{len(lst)} versões registradas para o modelo, {mod.nome_mod}."
    return render_template("/vers/vers_read_mod.html", msg=msg, lst=lst, mod=mod)

@bp_vers.route("/vers_edit")
def vers_edit():
    vers_dao = VersaoDao()
    lst = vers_dao.select_vers_az()

    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az()

    if not lst:
        msg = "Não há versões na database."
    else:
        msg = f"{len(lst)} versões listadas na database."
    return render_template("/vers/vers_edit.html", lst=lst, lst_mod=lst_mod, msg=msg)

@bp_vers.route("/vers_edit_mod", methods=["POST"])
def vers_edti_mod():
    cod_mod = request.form["cod_mod"]

    vers_dao = VersaoDao()
    lst = vers_dao.select_vers_mod_az(cod_mod)

    mod_dao = ModeloDao()
    mod = mod_dao.select_mod_id(cod_mod)
    if not lst:
        msg = f"Não há versões registradas para o modelo {mod.nome_mod}."
    else:
        msg = f"{len(lst)} versões registradas para o modelo {mod.nome_mod}."
    return render_template("/vers/vers_edit_mod.html", msg=msg, lst=lst, mod=mod)

@bp_vers.route("/vers_dell/<int:cod>")
def vers_dell(cod):
    vers_dao = VersaoDao()
    vers_dao.dell_vers(cod)

    if not vers_dao.select_vers_id(cod):
        msg += " | Versão excluída da database."
    else:
        msg += " | Erro ao exluir versão."

    lst = vers_dao.select_vers_az()
    
    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az()

    return render_template("/vers/vers_edit.html", msg=msg, lst=lst, lst_mod=lst_mod)

@bp_vers.route("/vers_update/<int:cod>")
def vers_form_update(cod):
    vers_dao = VersaoDao()
    vers = vers_dao.select_vers_id(cod)

    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az()
    return render_template("/vers/vers_update.html", vers=vers, msg="", display="none", lst_mod=lst_mod)

@bp_vers.route("/vers_save_update", methods=["POST"])
def vers_save_update():
    vers = Versao()
    vers.id_vers = request.form["id_vers"]
    vers.nome_vers = request.form["nome_vers"]
    vers.vlr_vers = request.form["vlr_vers"]
    vers.img_vers = request.form["img_vers"]
    vers.cod_mod = request.form["cod_mod"]

    vers_dao = VersaoDao()
    vers_dao.update_vers(vers)

    msg = f"Versão, {vers.nome_vers}, atualizada."

    mod_dao = ModeloDao()
    lst_mod = mod_dao.select_mod_az()
    return render_template("/vers/vers_update.html", vers=vers, msg=msg, display="block", lst_mod=lst_mod)
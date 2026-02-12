from flask import Blueprint, render_template, request
from dao.mod_dao import Modelo, ModeloDao
from dao.mont_dao import MontadoraDao

bp_mod = Blueprint("mod", __name__)

@bp_mod.route("/mod_form_create")
def mod_form_create():
    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()
    return render_template("/mod/mod_form_create.html", msg="", display="none", lst_mont=lst_mont)

@bp_mod.route("/mod_create", methods=["POST"])
def mod_create():
    mod = Modelo()
    mod.nome_mod = request.form["nome_mod"]
    mod.cod_mont = request.form["cod_mont"]

    mod_dao = ModeloDao()
    mod_dao.add_mod(mod)

    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()

    if not mod_dao.select_mod_id(mod.id_mod):
        msg = "Erro ao isnerir modelo."
    else:
        msg = f"Modelo, {mod.nome_mod}, adicionado para a montadora."
    return render_template("/mod/mod_form_create.html", msg=msg, display="block", lst_mont=lst_mont)

@bp_mod.route("/mod_read")
def mod_read():
    mod_dao = ModeloDao()
    lst = mod_dao.select_mod_az()

    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()
    if not lst:
        msg = "Não há modelos registrados na database."
    else:
        msg = f"{len(lst)} modelos registrados na database."
    return render_template("/mod/mod_read.html", msg=msg, lst=lst, lst_mont=lst_mont)

@bp_mod.route("/mod_read_mont", methods=["POST"])
def mod_read_mont():
    cod_mont = request.form["cod_mont"]

    mod_dao = ModeloDao()
    lst = mod_dao.select_mod_mont_az(cod_mont)

    mont_dao = MontadoraDao()
    mont = mont_dao.select_mont_id(cod_mont)
    if not lst:
        msg = f"Não há modelos registrados para a montadora, {mont.sgl_mont} - {mont.nome_mont}."
    else:
        msg = f"{len(lst)} modelos registrados para a montadora, {mont.sgl_mont} - {mont.nome_mont}"
    return render_template("/mod/mod_read_mont.html", msg=msg, lst=lst, mont=mont)

@bp_mod.route("/mod_edit")
def mod_edit():
    mod_dao = ModeloDao()
    lst = mod_dao.select_mod_az()

    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()
    if not lst:
        msg = "Não há modelos registrados na database."
    else:
        msg = f"{len(lst)} modelos registrados na database."
    return render_template("/mod/mod_edit.html", msg=msg, lst=lst, lst_mont=lst_mont)

@bp_mod.route("/mod_edit_mont", methods=["POST"])
def mod_edit_vers():
    cod_mont = request.form["cod_mont"]

    mod_dao = ModeloDao()
    lst = mod_dao.select_mod_mont_az(cod_mont)

    mont_dao = MontadoraDao()
    mont = mont_dao.select_mont_id(cod_mont)
    if not lst:
        msg = f"Não há modelos registrados para a montadora, {mont.sgl_mont} - {mont.nome_mont}."
    else:
        msg = f"{len(lst)} modelos registrados para a montadora, {mont.sgl_mont} - {mont.nome_mont}"
    return render_template("/mod/mod_edit_mont.html", msg=msg, lst=lst, mont=mont)

@bp_mod.route("/mod_dell/<int:cod>")
def mod_dell(cod):
    mod_dao = ModeloDao()
    mod_dao.dell_mod(cod)

    if not mod_dao.select_mod_id(cod):
        msg = "Modelo excluído da database."
    else:
        msg = "Erro ao excluir modelo."
    lst = mod_dao.select_mod_az()
    if not lst:
        msg +=" | Não há modelos registrados na database."
    else:
        msg +=f" | {len(lst)} modelos registrados na database."

    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()
    return render_template("/mod/mod_edit.html", msg=msg, lst=lst, lst_mont=lst_mont)

@bp_mod.route("/mod_update/<int:cod>")
def mod_form_update(cod):
    mod_dao = ModeloDao()
    mod = mod_dao.select_mod_id(cod)

    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()
    return render_template("/mod/mod_update.html", mod=mod, msg="", display="none", lst_mont=lst_mont)

@bp_mod.route("/mod_save_update", methods=["POST"])
def mod_save_update():
    mod = Modelo()
    mod.id_mod = request.form["id_mod"]
    mod.nome_mod = request.form["nome_mod"]
    mod.cod_mont = request.form["cod_mont"]

    mod_dao = ModeloDao()
    mod_dao.update_mod(mod)

    mont_dao = MontadoraDao()
    lst_mont = mont_dao.select_mont_az()

    msg = f"Modelo, {mod.nome_mod}, atualizado."
    return render_template("/mod/mod_update.html", msg=msg, mod=mod, display="block", lst_mont=lst_mont)
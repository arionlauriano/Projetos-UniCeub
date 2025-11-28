from flask import Blueprint, render_template, request
from dao.cli_dao import Cliente, ClienteDao
from dao.uf_dao import UFdao

bp_cli = Blueprint("cli", __name__)

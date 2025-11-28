from flask import Blueprint, render_template, request
from dao.uf_dao import UF, UFdao

bp_uf = Blueprint("uf", __name__)

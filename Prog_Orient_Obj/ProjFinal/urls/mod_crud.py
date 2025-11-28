from flask import Blueprint, render_template, request
from dao.mod_dao import Modelo, ModeloDao
from dao.mont_dao import MontadoraDao

bp_mod = Blueprint("mod", __name__)
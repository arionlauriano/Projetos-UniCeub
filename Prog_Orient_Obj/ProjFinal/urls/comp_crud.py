from flask import Blueprint, render_template, request
from dao.comp_dao import Compra, CompraDao
from dao.cli_dao import ClienteDao
from dao.vers_dao import VersaoDao

bp_comp = Blueprint("comp", __name__)

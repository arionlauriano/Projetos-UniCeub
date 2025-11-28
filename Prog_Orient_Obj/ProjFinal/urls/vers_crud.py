from flask import Blueprint, render_template, request
from dao.vers_dao import Versao, VersaoDao
from dao.mod_dao import ModeloDao

bp_vers = Blueprint("vers", __name__)
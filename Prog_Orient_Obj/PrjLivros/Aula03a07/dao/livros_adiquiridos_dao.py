import mysql.connector

from Autores_dao import AutoresDAO

class Livros_Ad:
    def __init__(self, cod_livro=None, nome_livro="", id_autor=None, id_editora=None):
        
        
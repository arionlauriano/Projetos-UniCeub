import mysql.connector

from Autores_dao import AutoresDAO
from Editoras_dao import EditorasDAO

class Livros_Ad:
    def __init__(self, cod_livro=None, nome_livro="", id_autor=None, id_editora=None):
        self.cod_livro=cod_livro
        self.nome_livro=nome_livro
        self.id_autor=id_autor
        self.id_editora=id_editora

    def __str__(self):
        return f"Id Livro: {self.cod_livro} Nome Livro {self.nome_livro} Id Autor: {self.id_autor} Id Editora: {self.id_editora}"

class Livros_AdDAO:
    def __init__(self, host="localhost", user="root", password="Senha#", database="colecao_livros"):
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexao.cursor()
        print("Conexão com a database estabelecida.")

    def selecionar(self, Livros_Ad):
        if not Livros_AdDAO.conexao:
            print("Sem conexão com a database.")
            return
        sql = "SELECT * FROM livros_adiquiridos"
        lista_livrosAd = []
        try:
            self.cursor.execute(sql)
            todosLivrosAd = self.cursor.fetchall()
            for row in todosLivrosAd:
                livros = Livros_Ad(cod_livro=row[0], nome_livro=row[1], id_autor=row[3], id_editora=row[4])
                lista_livrosAd.append(todosLivrosAd)
                return lista_livrosAd
        except mysql.connector.Error as err:
            print("Erro ao consultar tabela.")
            return []
        
    def inserir_livros(self, Livros_Ad):
        if not mysql.connector:
            return "Sem conexão com a database."
        sql = "INSERT INTO livros_adiquiridos (nome_livro, id_autor, id_editora) VALUES (%s, %s, %s)"
        values = [Livros_Ad.nome_livro, Livros_Ad.id_autor, Livros_Ad.id_editora]
        try:
            self.cursor.execute(sql, values)
            Livros_Ad.cod_livro = self.cursor.lastrowid
            print(f"Livro, {Livros_Ad.nome_livro}, inserido à tabela com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir livro a database: {err}")
            return

    def atualizar_livros(self, Livros_Ad):
        

        
if __name__ == "__main__":
    dao = Livros_AdDAO()

import mysql.connector

from dao.Autores_dao import AutoresDAO

class Livros_Ad:
    def __init__(self, cod_livro=None, nome_livro="", id_autor=None, autor=None):
        self.cod_livro=cod_livro
        self.nome_livro=nome_livro
        self.id_autor=id_autor
        self.autor = autor

    def __str__(self):
        return f"| Id Livro: {self.cod_livro} | Nome Livro {self.nome_livro} | Id Autor: {self.id_autor} | Nome Autor: {self.autor}"

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

    def selecionar(self):
        if not self.conexao:
            print("Sem conexão com a database.")
            return
        sql = "SELECT * FROM livros_adiquiridos ORDER BY nome_livro"
        try:
            self.cursor.execute(sql)
            todosLivrosAd = self.cursor.fetchall()
            lst_livra = []
            daoAutores = AutoresDAO()
            for row in todosLivrosAd:
                autor = daoAutores.consulta_por_id(row[2])
                livros = Livros_Ad(cod_livro=row[0], nome_livro=row[1], id_autor=row[2], autor=autor.nome_autor)
                lst_livra.append(livros)
        except mysql.connector.Error as err:
            print("Erro ao consultar tabela.")
            return []
        return lst_livra
    
    def consulta_id(self, cod_livro):
        if not self.conexao:
            return None
        sql = "SELECT * FROM livros_adiquiridos WHERE cod_livro=%s"

        try:
            self.cursor.execute(sql, [cod_livro])
            resultado = self.cursor.fetchone()
            if resultado is None:
                return None
            else:
                aut_dao = AutoresDAO()
                autor = aut_dao.consulta_por_id(resultado[2])
                livro=Livros_Ad(cod_livro=resultado[0], nome_livro=resultado[1], id_autor=resultado[2], autor=autor)
                return livro
        except mysql.connector.Error as err:
            print(f"Erro:{err}")
            return []

        
    def inserir_livros(self, Livros_Ad):
        if not mysql.connector:
            return "Sem conexão com a database."
        sql = "INSERT INTO livros_adiquiridos (nome_livro, id_autor) VALUES (%s, %s)"
        values = [Livros_Ad.nome_livro, Livros_Ad.id_autor]
        try:
            self.cursor.execute(sql, values)
            self.conexao.commit()
            Livros_Ad.cod_livro = self.cursor.lastrowid
            print(f"Livro, {Livros_Ad.nome_livro}, inserido à tabela com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir livro a database: {err}")
            return
        
    def atualizar_livros(self, Livros_Ad):
        if not mysql.connector:
            return "Sem conexão com a database."
        sql = "UPDATE livros_adiquiridos SET nome_livro=%s WHERE cod_livro=%s"
        valores = [Livros_Ad.nome_livro, Livros_Ad.cod_livro]
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Autor de código {Livros_Ad.id_autor} atualizado.")
        except mysql.connector.Error as err: 
            return f"Erro ao atulaizar registro"
        
    def deletar_livros(self, cod_livro):
        if not mysql.connector:
            return "Sem conexão com a database."
            
        sql = "DELETE FROM livros_adiquiridos WHERE cod_livros=%s"

        try:
            self.cursor.execute(sql, [cod_livro])
            self.conexao.commit()
            print(f"Autor de código {cod_livro} deletado.")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar autor de código {cod_livro}: {err}")
            self.conexao.rollback()
            return False



        
if __name__ == "__main__":
    dao = Livros_AdDAO()

    if dao.conexao:
        print("\nLivros Adquiridos:")
        print(dao.consulta_id(1))

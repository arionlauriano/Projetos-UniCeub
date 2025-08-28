import mysql.connector

class Autores:
    def __init__(self, nome_autor="", cod_autor=None):
        self.nome_autor = nome_autor
        self.cod_autor = cod_autor

    def __str__(self):
        return f"Id: {self.cod_autor}, Nome: {self.nome_autor}"
    
class AutoresDAO:
    def __init__(self, host="localhost", user="root", password="Senha#", database="colecao_livros"):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
            print("Conexão com a database estabelecida.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar com a database: {err}")
            self.conexao = None
            self.cursor = None

    def inserir_autores(self, Autores):
        if not self.conexao:
            return
        
        sql = "INSERT INTO autores (nome_autor) VALUES (%s)"

        try:
            self.cursor.execute(sql, [Autores.nome_autor])
            self.conexao.commit()
            print(f"Autor {Autores.nome_autor} inserido.")
            Autores.cod_autor = self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao inserir autor, {Autores.nome_autor}: {err}")

    def select_alfabetico(self):
        if not self.conexao:
            return
        
        sql = "SELECT * FROM autores ORDER BY nome_autor"

        try:
           self.cursor.execute(sql)
           resultados = self.cursor.fetchall()

           lista_autores = []




if __name__ == "__main__":
    dao = AutoresDAO()

        
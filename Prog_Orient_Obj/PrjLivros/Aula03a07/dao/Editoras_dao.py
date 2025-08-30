import mysql.connector

class Editoras: 
    def __init__(self, cod_editora=None, nome_editora=""):
        self.cod_editora = cod_editora
        self.nome_editora = nome_editora
    
    def __str__(self):
        return f"Id: {self.cod_editora} Nome: {self.nome_editora}"
    
class EditorasDAO:
    def __init__(self, host="localhost", user="root", password="Senha#", database="colecao_livros"):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
            )
            self.cursor = self.conexao.cursor()
            print("Conexão com o banco de dados estabelecida.")
        except mysql.connector.Error as err:
            print(f"Erro ao connectar ao banco de dados: {err}")
            self.conexao = None
            self.cursor = None

    def inserir(self, Editoras):
        if not self.conexao:
            ("Sem conexão")
            return
        sql = "INSERT INTO editoras (nome_editora) VALUES (%s)"
        try:
            self.cursor.execute(sql, Editoras.nome_editora)
            print(f"Editora {Editoras.nome_editora} adicionada.")
            Editoras.cod_editora = self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao inserir editora: {err}")

        
    
        

if __name__ == "__main__":
    EditorasDAO()

    if EditorasDAO.conexao:
        editora1= Editoras("alguma editora")
        
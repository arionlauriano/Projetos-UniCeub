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
            print("10conectado")
            return []
        
        sql = "SELECT * FROM autores ORDER BY nome_autor"

        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            lista_autores = []
            for row in resultados:
               autores = Autores(cod_autor=row[0], nome_autor=row[1])
               lista_autores.append(autores)
            return lista_autores
        except mysql.connector.Error as err:
            print(f"Erro ao selecionar autores: {err}")
            return []
        
    def consulta_por_id(self, cod_autor):
        if not self.conexao:
            return None
        sql = "SELECT * FROM autores WHERE cod_autor=%s"

        try:
            self.cursor.execute(sql, [cod_autor])
            resultado = self.cursor.fetchone()
            if resultado is None:
                return None
            else:
                autor=Autores(cod_autor=resultado[0], nome_autor=resultado[1])
                return autor
        except mysql.connector.Error as err:
            return None
        
    def atualizar(self, autor):
        if not self.conexao:
            return
        
        sql = "UPDATE autores SET nome_autor=%s WHERE cod_autor=%s"
        valores = (autor.nome_autor, autor.cod_autor)

        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Autor de código {autor.cod_autor} atualizado.")
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar autor de código {Autores.cod_autor}: {err}")
            self.conexao.rollback()

    def deletar(self, cod_autor):
        if not self.conexao:
            return
        
        sql = "DELETE FROM autores WHERE cod_autor=%s"

        try:
            self.cursor.execute(sql, [cod_autor])
            self.conexao.commit()
            print(f"Autor de código {cod_autor} deletado.")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar autor de código {cod_autor}: {err}")
            self.conexao.rollback()


if __name__ == "__main__":
    dao = AutoresDAO()

    if dao.conexao:
        autor1=Autores("Philip Pullman")
        autor2=Autores("Agatha Christie")

        dao.inserir_autores(autor1)
        dao.inserir_autores(autor2)

        print("\nAutores Cadastrados:")
        for autor in dao.select_alfabetico():
            print(autor)

        if autor1.cod_autor:
            print(f"\nAtualizando autor de código {autor1.cod_autor}...")
            autor1.nome_autor="Jorge"
            dao.atualizar(autor1)

        if autor2.cod_autor:
            print(f"\nDeletando autor de código {autor2.cod_autor}...")
            dao.deletar(autor2.cod_autor)

        print("\nLista Atualizada:")
        print(dao.consulta_por_id(1))

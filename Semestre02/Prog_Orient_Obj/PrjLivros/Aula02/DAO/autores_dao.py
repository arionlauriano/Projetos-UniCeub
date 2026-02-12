import mysql.connector

# Definição da classe:
class autores:
    # Inicializa os Atributos
        # Ele pega e define qual atributo chamar?
    def __init__(self, nome_autor="", cod_autor= None):
        self.cod_autor = cod_autor
        self.nome_autor = nome_autor
    def __str__(self):
        return f"Id: {self.cod_autor} Nome: {self.nome_autor}"
    
# Definição da classe que cuidará das operações dentro do manco de dados
class autoresDAO:
# Faz a conexão 
    def __init__(self, host="localhost", user="root", password="Senha#", database="colecao_livros"):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
            print("Conexão com o banco de dados estabelecida.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar com a database: {err}")
            self.conexao = None
            self.cursor = None
# Método para inserir um novo objeto
    def inserir(self, autores):
        # Ele não vai nem tentar se não houver conexão
        if not self.conexao:
            print("Erro: não há conexão com a database.")
            return # Encerra o processamento da função "inserir()"
    
        sql = "INSERT INTO autores (nome_autor) VALUES (%s)"
        valores = [autores.nome_autor]
        # Try faz teste e caso não haja erro o except é ignorado
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Autor '{autores.nome_autor}' foi inserido.")
            autores.cod_autor = self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao inserir Autor; {err}")
            self.conexao.rollback()

    def selecionar_tudo(self):
        #Vai dar o "SELECT * FROM autores;"
        if not self.conexao:
            print("Erro: Nenhuma conexão com a database.")
            return
        sql = "SELECT * FROM autores"

        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()

            lista_autores = []
            for row in resultados:
                Autores = autores(cod_autor=row[0], nome_autor=row[1])
                lista_autores.append(Autores)

            return lista_autores
        except mysql.connector.Error as err:
            print(f"Erro ao selecionar autores: {err}")
    
    # Vai fazer o UPDATE de um dos autores previamente registrados
    def atualizar(self, autores):
        if not self.conexao:
            print("Erro: Nenhuma conexão com a database.")
            return
        
        sql = "UPDATE autores SET nome_autor = %s WHERE cod_autor = %s"
        valores = [autores.nome_autor, autores.cod_autor]

        try:
            self.cursor.execute(sql,valores)
            self.conexao.commit()
            print(f"Autor de código {autores.cod_autor} atualizado.")
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar montadora: {err}")
            self.conexao.rollback()

    def deletar(self, autores):
        if not self.conexao:
            print("Erro: sem conexão com a database.")
            return
        
        sql = "DELETE FROM autores WHERE cod_autor=%s"

        try:
            self.cursor.execute(sql,[autores.cod_autor])
            self.conexao.commit()
            print(f"Autor de código {autores.cod_autor} deletado.")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar autor:{err}")
            self.conexao.rollback()


# Chamado das funções
if __name__ == "__main__":
    #roda a função autoresDAO() estabelecendo conexão
    dao = autoresDAO()

    if dao.conexao:
        # Caso a conexão exista, cria objetos Autores
        autor1= autores("Philip Pullman")
        autor2= autores("J.K.Rowling")

        # Usa a função inserir()
        dao.inserir(autor1)
        dao.inserir(autor2)

        # Usa o DAO para fazer o "SELECT * FROM autroes;"
        print("\nAutores cadastrados:")
        todos_autores = dao.selecionar_tudo()
        for autor in todos_autores:
            print(autor)

        # Usa a função atualizar()
        if autor1.cod_autor:
        # Busca o código do autor1
            print(f"\nAtualizando o autor de ID {autor1.cod_autor}...")
            autor1.nome_autor = "Ken Foulett"
            # Atualiza o nome_autor do objeto autor1
            dao.atualizar(autor1)
            # Chama a função para atualizar o objeto autor1
        
        # Busca o id do autor2:
        if autor2.cod_autor:
            print(f"\nDeletando autor de código {autor2.cod_autor}")
            # Chama a função deletar() para o autor2
            dao.deletar(autor2)

        print("\n Atuores cadastrados:")
        todos_autores = dao.selecionar_tudo()
        for autor in todos_autores:
            print(autor)


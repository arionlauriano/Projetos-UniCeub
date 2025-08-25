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
    
    sql = "INSERT INTO autores (nome_autores) VALUES (%s)"
    valores = (autores.nome_autor)
    # Try faz teste e caso não haja erro o except é ignorado
    try:
        self.cursor.execute(sql, valores)
        self.cursor.commit()
        print(f"Autor '{autor.nome_autor}' foi inserido.")
        autor.cod_autor = self.curoso.lastrowid
    except mysql.connecotr.Error as err:
        print(f"Erro ao inserir montadora; {err}")
        self.conexao.rollback()


if __name__ == "__main__":
    #roda a função autoresDAO() estabelecendo conexão
    dao = autoresDAO()

    # Caso a conexão exista, cria objetos Autores
    autor1= autores("J.K. Rouling")

    # Usa a função inserir()
    dao.inserir(autor1)
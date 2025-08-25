import mysql.python

# Definição da classe:
class autores:
    # Inicializa os Atributos
        # Ele pega e define qual atributo chamar?
    def __init__(self, cod_autor= None, nome_autor=""):
        self.cod_autor = cod_autor
        self.nome_autor = nome_autor
    def __str__(self):
        return f"Id: {self.cod_autor} Nome: {self.nome_autor}"
    
# Definição da conexão com a database
class autoresDAO:
    def __init__(self, host="localhost", user="root", password="atuasenha", database="colecao_livros"):
    
    self.conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
        )
    self.cursor = self.conexao.cursor()
    print("Conexão com o banco de dados estabelecida.")
    self.conexao = None
    self.cursor = None
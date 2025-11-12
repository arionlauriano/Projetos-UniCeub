import mysql.connector
from uf_dao import UF, UFdao

class Cliente:
    def __init__(self, id_cli=None, nome_cli="", data_nasc_cli="", cod_uf=None, cep_cli="", end_cli="", uf=None):
        self.id_cli=id_cli
        self.nome_cli=nome_cli
        self.data_nasc_cli=data_nasc_cli
        self.cod_uf=cod_uf
        self.cep_cli=cep_cli
        self.end_cli=end_cli
        self.uf=uf
    
    def __str__(self):
        return f"ID Cliente: {self.id_cli} || Nome Cliente: {self.nome_cli} || Data de Nascimento: {self.data_nasc_cli} || Codigo UF: {self.cod_uf} || Sigla UF: {self.uf.sgl_uf} || Nome UF: {self.uf.nome_uf} || CEP Cliente: {self.cep_cli} || Endereço Cliente: {self.end_cli}"
    
class ClienteDao:
    def __init__(self, host="localhost", user="root", database="db_auto", password="Senha#"):
        try:
            self.conexao=mysql.connector.connect(
                host=host,
                user=user,
                database=database,
                password=password
            )
            self.cursor=self.conexao.cursor()
            if self.conexao:
                print("Conexão estabelecida com a database.")
        except mysql.connector.Error as err:
            return f"Erro: {err}"
    
    def add_cli(self, cli):
        if not self.conexao:
            return None
        
        sql="INSERT INTO cliente (nome_cli, data_nasc_cli, cod_uf, cep_cli, end_cli) VALUES (%s,%s,%s,%s,%s)"
        valores = (cli.nome_cli, cli.data_nasc_cli, cli.cod_uf, cli.cep_cli, cli.end_cli)

        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()

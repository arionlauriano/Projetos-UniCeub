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
            return None
    
    def add_cli(self, cli):
        if not self.conexao:
            return None
        
        sql="INSERT INTO cliente (nome_cli, data_nasc_cli, cod_uf, cep_cli, end_cli) VALUES (%s,%s,%s,%s,%s)"
        valores = (cli.nome_cli, cli.data_nasc_cli, cli.cod_uf, cli.cep_cli, cli.end_cli)

        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            cli.id_cli=self.cursor.lastrowid
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def update_cli(self, cli):
        if not self.conexao:
            return None
        
        sql="UPDATE cliente SET nome_cli=%s, data_nasc_cli=%s, cod_uf=%s, cep_cli=%s, end_cli=%s WHERE id_cli=%s"
        valores=[cli.nome_cli, cli.data_nasc_cli, cli.cod_uf, cli.cep_cli, cli.end_cli, cli.id_cli]
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
    
    def dell_cli(self, id_cli):
        sql="DELETE FROM cliente WHERE id_mod=%s"
        try:
            self.cursor.execute(sql, [id_cli])
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def select_cli_az(self, cod_uf):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM cliente"
        try:
            self.cursor.execute(sql)
            td_cli=self.cursor.fetchall()
            lst_cli = []
            uf_dao=UFdao()
            for row in td_cli:
                uf=uf_dao.select_uf_id(row[3])
                cli=Cliente(id_cli=row[0], nome_cli=row[1], data_nasc_cli=row[2], cod_uf=row[3], cep_cli=row[4], end_cli=row[5], uf=uf)
                lst_cli.append(cli)
        except mysql.connector.Error as err:
            lst_cli=None
            return f"Erro: {err}"
        return lst_cli
    
    def select_cli_id(self, id_cli):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM cliente WHERE id_cli=%s"
        try:
            self.cursor.execute(sql, [id_cli])
            result=self.cursor.fetchone()
            if result is None:
                return None
            else:
                uf_dao=UFdao()
                uf=uf_dao.select_uf_id(result[5])
                cli=Cliente(id_cli=result[0], nome_cli=result[1], data_nasc_cli=result[2], cod_uf=result[3], cep_cli=result[4], end_cli=result[5], uf=uf)
                return cli
        except mysql.connector.Error as err:
            return f"Erro: {err}"
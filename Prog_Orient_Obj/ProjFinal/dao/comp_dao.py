import mysql.connector
from vers_dao import Versao, VersaoDao
from cli_dao import Cliente, ClienteDao
from uf_dao import UF, UFdao

class Compra:
    def __init__(self, id_comp=None, data_comp="", cod_nf_comp="", total_comp="", cod_cli=None, cod_vers=None, cli=None, vers=None):
        self.id_comp=id_comp
        self.data_comp=data_comp
        self.cod_nf_comp=cod_nf_comp
        self.total_comp=total_comp
        self.cod_cli=cod_cli
        self.cod_vers=cod_vers
        self.cli=cli
        self.vers=vers

    def __str__(self):
        return f"ID Compra: {self.id_comp} || Data: {self.data_comp} || NF: {self.cod_nf_comp} || Total: {self.total_comp} || Codigo Cliente: {self.cod_cli} || Codigo Versão: {self.cod_vers} || Nome Cliente: {self.cli.nome_cli} || Data de Nascimento: {self.cli.data_nasc_cli} || Codigo UF: {self.cli.cod_uf} || CEP: {self.cli.cep_cli} || Endereço: {self.cli.end_cli} || Nome Versão: {self.vers.nome_vers} || IMG: {self.vers.img_vers} || Código Modelo: {self.vers.cod_mod}"
    
class CompraDao:
    def __init__(self, host="localhost", user="root", database="db_auto", password="Senha#"):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                database=database,
                password=password
                )
            self.cursor = self.conexao.cursor()
            if self.conexao:
                print("Conexao estabelecida com a database.")
        except mysql.connector.Error as err:
            return None
        
    def add_comp(self, comp):
        if not self.conexao:
            return None
        
        sql="INSERT INTO compra (data_comp, cod_nf_comp, total_comp, cod_cli, cod_vers) VALUES (%s, %s, %s, %s, %s)"
        valores=(comp.data_comp, comp.cod_nf_comp, comp.total_comp, comp.cod_cli, comp.cod_vers)
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
    
    def update_comp(self, comp):
        if not self.conexao:
            return None
        
        sql="UPDATE comp SET data_comp=%s, cod_nf_comp=%s, total_comp=%s, cod_cli=%s, cod_vers=%s WHERE id_comp=%s"
        valores=(comp.data_comp, comp.cod_nf_comp, comp.total_comp, comp.cod_cli, comp.cod_vers, comp.id_comp)
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        
    def dell_comp(self, id_comp):
        if not self.conexao:
            return None
        
        sql="DELETE FROM compra WHERE id_comp=%s"
        try:
            self.cursor.execute(sql, [id_comp])
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def select_comp_az(self):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM compra ORDER BY data_comp"
        try:
            self.cursor.execute(sql)
            td_comp=self.cursor.fetchall()
            lst_comp=[]
            cli_dao=ClienteDao()
            vers_dao=VersaoDao()
            for row in td_comp:
                cli=cli_dao.select_cli_id(row[4])
                vers=vers_dao.select_vers_id(row[5])
                comp=Compra(id_comp=row[0], data_comp=row[1], cod_nf_comp=row[2], total_comp=row[3], cod_cli=row[4], cod_vers=row[5], cli=cli, vers=vers)
                lst_comp.append(comp)
        except mysql.connector.Error as err:
            lst_comp=None
            return f"Erro: {err}"
        return lst_comp
    
    def select_comp_cli_az(self, cod_cli):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM compra WHERE cod_cli=%s ORDER BY data_comp, cod_vers"
        try:
            self.cursor.execute(sql, [cod_cli])
            td_comp=self.cursor.fetchall()
            lst_comp=[]
            cli_dao=ClienteDao()
            vers_dao=VersaoDao()
            for row in td_comp:
                cli=cli_dao.select_cli_id(row[4])
                vers=vers_dao.select_vers_id(row[5])
                comp=Compra(id_comp=row[0], data_comp=row[1], cod_nf_comp=row[2], total_comp=row[3], cod_cli=row[4], cod_vers=row[5], cli=cli, vers=vers)
                lst_comp.append(comp)
        except mysql.connector.Error as err:
            lst_comp=None
            return f"Erro: {err}"
        return lst_comp
    
    def select_comp_vers_az(self, cod_vers):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM compra WHERE cod_vers=%s ORDER BY data_comp, cod_cli"
        try:
            self.cursor.execute(sql, [cod_vers])
            td_comp=self.cursor.fetchall()
            lst_comp=[]
            cli_dao=ClienteDao()
            vers_dao=VersaoDao()
            for row in td_comp:
                cli=cli_dao.select_cli_id(row[4])
                vers=vers_dao.select_vers_id(row[5])
                comp=Compra(id_comp=row[0], data_comp=row[1], cod_nf_comp=row[2], total_comp=row[3], cod_cli=row[4], cod_vers=row[5], cli=cli, vers=vers)
                lst_comp.append(comp)
        except mysql.connector.Error as err:
            lst_comp=None
            return f"Erro: {err}"
        return lst_comp 
    
    def select_comp_id(self, id_comp):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM compra WHERE id_comp=%s"
        try:
            self.cursor.execute(sql, [id_comp])
            result=self.cursor.fetchone()
            if result is None:
                return None
            else:
                cli_dao=ClienteDao()
                vers_dao=VersaoDao()
                cli=cli_dao.select_cli_id(result[4])
                vers=vers_dao.select_vers_id(result[5])
                comp=Compra(id_comp=result[0], data_comp=result[1], cod_nf_comp=result[2], total_comp=result[3], cod_cli=result[4], cod_vers=result[5], cli=cli, vers=vers)
                return comp
        except mysql.connector.Error as err:
            return f"Erro: {err}"
    
if __name__=="__main__":
    comp_dao=CompraDao()
    
    if comp_dao.conexao:
        comp1=Compra(data_comp="2001-01-01", cod_nf_comp="123", total_comp="456", cod_cli="2", cod_vers="3")
        comp2=Compra(data_comp="2002-01-01", cod_nf_comp="1234", total_comp="4567", cod_cli="2", cod_vers="4")

        comp_dao.add_comp(comp1)
        comp_dao.add_comp(comp2)

        print("\n Teste select_cli_comp:")
        for comp in comp_dao.select_comp_cli_az(2):
            print(comp)

        print("\n Teste select_vers_comp:")
        for comp in comp_dao.select_comp_vers_az(4):
            print(comp)

        print("\n Teste select_comp_id:")
        print(comp_dao.select_comp_id(1))

        comp_dao.dell_comp(comp1.id_comp)

        comp2.cod_nf_comp="testeUpdate"
        comp_dao.update_comp(comp2)

        print("\n Teste select_comp_az:")
        for comp in comp_dao.select_comp_az():
            print(comp)
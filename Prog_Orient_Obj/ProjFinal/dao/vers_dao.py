import mysql.connector
from mod_dao import Modelo, ModeloDao

class Versao:
    def __init__(self, id_vers=None, nome_vers="", vlr_vers="", img_vers="", cod_mod=None, mod=None):
        self.id_vers=id_vers
        self.nome_vers=nome_vers
        self.vlr_vers=vlr_vers
        self.img_vers=img_vers
        self.cod_mod=cod_mod
        self.mod=mod
    
    def __str__(self):
        return f"ID Versão: {self.id_vers} || Nome Versão: {self.nome_vers} || Valor Versão: R${self.vlr_vers} || Endereço Img: {self.img_vers} || Cdigo Modelo: {self.cod_mod} || Nome Modelo: {self.mod.nome_mod}"
    
class VersaoDao:
    def __init__(self, host="localhost", user="root", database="db_auto", password="Senha#"):
        try:
            self.conexao= mysql.connector.connect(
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
        
    def add_vers(self, vers):
        if not self.conexao:
            return None
        
        sql="INSERT INTO versao (nome_vers, vlr_vers, img_vers, cod_mod)"
        valores = (vers.nome_vers, vers.vlr_vers, vers.img_vers, vers.cod_mod)
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            vers.id_vers=self.cursor.lastrowid
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def update_vers(self, vers):
        if not self.conexao:
            return None
        
        sql="UPDATE versao SET nome_vers=%s, vlr_vers=%s, img_vers=%s, cod_mod=%s WHERE id_vers=%s"
        valores=(vers.nome_vers, vers.vlr_vers, vers.img_vers, vers.cod_mod, vers.id_vers)
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def dell_vers(self, id_vers):
        if not self.conexao:
            return None
        
        sql="DELETE FROM versao WHERE id_vers=%s"
        try:
            self.cursor.execute(sql, [id_vers])
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def select_vers_az(self):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM versao ORDER BY cod_mod, nome_vers"
        try:
            self.cursor.execute(sql)
            td_vers=self.cursor.fetchall()
            lst_vers = []
            mod_dao = ModeloDao()
            for row in td_vers:
                mod=mod_dao.select_mod_id(row[4])
                vers=Versao(id_vers=row[0], nome_vers=row[1], vlr_vers=row[2], img_vers=row[3], cod_mod=row[4], mod=mod)
                lst_vers.append(vers)
        except mysql.connector.Error as err:
            lst_vers=None
            return f"Erro: {err}"
        return lst_vers
    
    def select_vers_mod_az(self, cod_mod):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM versao WHERE cod_mod=%s ORDER BY nome_vers"
        try:
            self.cursor.execute(sql, [cod_mod])
            td_vers=self.cursor.fetchall()
            lst_vers = []
            mod_dao = ModeloDao()
            for row in td_vers:
                mod=mod_dao.select_mod_id(row[4])
                vers=Versao(id_vers=row[0], nome_vers=row[1], vlr_vers=row[2], img_vers=row[3], cod_mod=row[4], mod=mod)
                lst_vers.append(vers)
        except mysql.connector.Error as err:
            lst_vers=None
            return f"Erro: {err}"
        return lst_vers
    
    def select_vers_id(self, id_vers):
        if not self.conexao:
            return None
        
        sql="SELECT * FROM vers WHERE id_vers=%s"
        try:
            self.cursor.execute(sql, [id_vers])
            result=self.cursor.fetchone()
            if result is None:
                return None
            else:
                mod_dao=ModeloDao()
                mod=mod_dao.select_mod_id(result[4])
                vers=Versao(id_vers=result[0], nome_vers=result[1], vlr_vers=result[2], img_vers=result[3], cod_mod=result[4], mod=mod)
                return vers
        except mysql.connector.Error as err:
            return f"Erro: {err}"
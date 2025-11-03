import mysql.connector
from mont_dao import Montadora, MontadoraDao

class Modelo:
    def __init__(self, id_mod=None, nome_mod="", cod_mont=None, mont=None):
        self.id_mod=id_mod
        self.nome_mod=nome_mod
        self.cod_mont=cod_mont
        self.mont=mont

    def __str__(self):
        return f"ID Modelo: {self.id_mod} || Nome Modelo: {self.nome_mod} || Código Montadora {self.cod_mont} || Sigla Montadora: {self.montadora.sgl_mont} || Nome Montadora: {self.montadora.nome_mont}"
    
class ModeloDao:
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
            return f"Erro: {err}"
    
    def add_mod(self, mod):
        if not self.conexao:
            return None
        
        sql= "INSERT INTO modelo (nome_mod, cod_mont) VALUES (%s,%s)"
        valores = (mod.nome_mod, mod.cod_mont)
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            mod.id_mod=self.cursor.lastrowid
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def update_mod(self, mod):
        if not self.conexao:
            return None
        
        sql= "UPDATE modelo SET nome_mod=%s, cod_mont=%s WHERE id_mod=%s"
        valor=(mod.nome_mod, mod.cod_mont, mod.id_mod)
        try:
            self.cursor.execute(sql, valor)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def dell_mod(self, id_mod):
        if not self.conexao:
            return None
        
        sql= "DLETE FROM modelo WHERE id_mod=%s"
        try:
            self.cursor.execute(sql, [id_mod])
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
    
    def select_mod_mont_az(self, cod_mont):
        if not self.conexao:
            return None 
        
        sql = "SELECT * FROM modelo WHERE cod_mont=%s ORDER BY nome_mod"
        try:
            self.cursor.execute(sql, [cod_mont])
            td_mod = self.cursor.fetchall()
            lst_mod = []
            for row in td_mod:
                mod=Modelo(id_mod=row[0], nome_mod=row[1], cod_mont=row[2])
                lst_mod.append(mod)
        except mysql.connetor.Error as err:
            lst_mod=None
            return f"Erro: {err}"
        return lst_mod
    

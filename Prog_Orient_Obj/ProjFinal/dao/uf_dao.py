import mysql.connector

class UF:
    def __init__(self, id_uf=None, sgl_uf="", nome_uf=""):
        self.id_uf=id_uf
        self.sgl_uf=sgl_uf
        self.nome_uf=nome_uf
    
    def __str__(self):
        return f"Id UF: {self.id_uf} || Sgl UF: {self.sgl_uf} || Nome UF: {self.nome_uf}"

class UFdao:
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
    
    def add_uf(self, uf):
        if not self.conexao:
            return False
        
        sql = "INSERT INTO uf (sgl_uf, nome_uf) VALUES (%s, %s)"
        valores = [uf.sgl_uf, uf.nome_uf]

        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            uf.id_uf = self.cursor.lastrowid
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def update_uf(self, uf):
        if not self.conexao:
            return False
        
        sql = "UPDATE uf SET sgl_uf = %s, nome_uf = %s WHERE id_uf = %s"
        valores = [uf.sgl_uf, uf.nome_uf, uf.id_uf]

        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"

    def dell_uf(self, id_uf):
        if not self.conexao:
            return False
        
        sql = "DELETE uf WHERE id_uf=%s"
        try:
            self.cursor.execute(sql, [id_uf])
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def select_uf_az(self):
        if not self.conexao:
            return False
        
        sql = "SELECT * FROM uf ORDER BY sgl_uf;"

        try:
            self.cursor.execute(sql)
            td_uf = self.cursor.fetchall()
            lst_uf = []
            for row in td_uf:
                uf=UF(id_uf=row[0], sgl_uf=row[1], nome_uf=row[2])
                lst_uf.append(uf)
        except mysql.connector.Error as err:
            lst_uf = None
            return f"Erro: {err}"
        return lst_uf
    
    def select_uf_id(self, id_uf):
        if not self.conexao:
            return None
        
        sql= "SELECT * FROM uf WHERE id_uf=%s"
        try:
            self.cursor.execute(sql, [id_uf])
            result=self.cursor.fetchone()
            if result is None:
                return None
            else:
                uf=UF(id_uf=result[0], sgl_uf=result[1], nome_uf=result[2])
        except mysql.connector.Error as err:
            uf=None
        return uf
    
if __name__ == "__main__":
    uf_dao = UFdao()

    if uf_dao.conexao:
        print("\n Lista de Estados:")
        for uf in uf_dao.select_uf_az():
            print(uf)

        print("\n Teste Select por ID: DF")
        print(uf_dao.select_uf_id(7))

        uf1 = UF(sgl_uf="SV", nome_uf="Samba da Virgínia")
        uf2 = UF(sgl_uf="TP", nome_uf="topezeira")
        uf_dao.add_uf(uf1)
        uf_dao.add_uf(uf2)

        print("\n Teste Adds:")
        for uf in uf_dao.select_uf_az():
            print(uf)

        uf_dao.dell_uf(3)

        uf2.nome_uf="Teste deu Certo"
        uf_dao.update_uf(uf2)

        print("\n Teste Dell e Update:")
        for uf in uf_dao.select_uf_az():
            print(uf) 

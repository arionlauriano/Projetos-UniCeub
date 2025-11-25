import mysql.connector
class Montadora:
    
    def __init__(self, id_mont=None, sgl_mont="", nome_mont=""):
        self.id_mont=id_mont
        self.sgl_mont=sgl_mont
        self.nome_mont=nome_mont
    
    def __str__(self):
        return f"Id Montadora: {self.id_mont} || Sgl Montadora: {self.sgl_mont} || Nome Montadora: {self.nome_mont}"
    
class MontadoraDao:
    def __init__(self, host="localhost", user="root", password="Senha#", database="db_auto"):
        try:
            self.conexao = mysql.connector.connect(
                host=host, 
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
            if self.conexao:
                print("Conexão estabaselecida com a database.")
        except mysql.connector.Error as err:
            print(f"Erro ao estabalecer conexão: {err}")


    def add_mont(self, mont):
        if not self.conexao:
            print( "Sem conexão com a database.")
            return False

        sql = "INSERT INTO montadora (sgl_mont, nome_mont) VALUES (%s,%s)" 
        values=[mont.sgl_mont, mont.nome_mont]
        try:
            self.cursor.execute(sql, values)
            self.conexao.commit()
            mont.id_mont=self.cursor.lastrowid
        except mysql.connector.Error as err:
            return False
        return True
    
    def update_mont(self, mont):
        if not self.conexao:
            return False
        
        sql="UPDATE montadora SET sgl_mont=%s, nome_mont=%s WHERE id_mont=%s"
        valores=(mont.sgl_mont, mont.nome_mont, mont.id_mont)

        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    def dell_mont(self, id_mont):
        if not self.conexao:
            return None
        
        sql="DELETE FROM montadora WHERE id_mont=%s"
        try:
            self.cursor.execute(sql,[id_mont])
            self.conexao.commit()
        except mysql.connector.Error as err:
            return f"Erro: {err}"

    #"az"= "a" to "b"
    def select_mont_az(self):
        if not self.conexao:
            return "Sem concexão com a database."
        sql = "SELECT * FROM montadora ORDER BY sgl_mont"

        try:
            self.cursor.execute(sql)
            td_mont = self.cursor.fetchall()
            lst_mont = []
            for row in td_mont:
                mont = Montadora(id_mont=row[0], sgl_mont=row[1], nome_mont=row[2])
                lst_mont.append(mont)
        except mysql.connector.Error as err:
            lst_mont=None
        return lst_mont
    
    def select_mont_id(self, id_mont):
        if not self.conexao:
            return None
        
        sql = "SELECT * FROM montadora WHERE id_mont=%s"
        valores=[id_mont]
        try:
            self.cursor.execute(sql, valores)
            result=self.cursor.fetchone()
            if result is None:
                return None
            else:
                montadora=Montadora(id_mont=result[0], sgl_mont=result[1], nome_mont=result[2])
                return montadora
        except mysql.connector.Error as err:
            return f"Erro: {err}"
        
    
    
# Smoke Test
if __name__ == "__main__":

    mont_dao=MontadoraDao()

    if mont_dao.conexao:
        mont1=Montadora(sgl_mont="VW", nome_mont="Volks Wagen")
        mont2=Montadora(sgl_mont="BYD", nome_mont="Build Your Dreams")
        mont3=Montadora(sgl_mont="H", nome_mont="Honda")
        mont_dao.add_mont(mont1)
        mont_dao.add_mont(mont2)
        mont_dao.add_mont(mont3)

        for mont in mont_dao.select_mont_az():
            print(mont)
        
        mont1.sgl_mont="GWM"
        mont1.nome_mont="Great Wall Motors"
        mont_dao.update_mont(mont1)
        mont_dao.dell_mont(3)

        print("\n Conferindo Updates e Delets")
        for mont in mont_dao.select_mont_az():
            print(mont)
        print("\n Select por id:")
        print(mont_dao.select_mont_id(2)) 
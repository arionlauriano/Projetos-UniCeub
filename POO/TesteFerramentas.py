import mysql.connector
from mysql.connector import Error


class MontadoraDAO:
   def __init__(self, host = 'localhost', database = 'db_auto', user = 'root', password = 'ceub123456'):
       self.host = host
       self.database = database
       self.user = user
       self.password = password
       self.connection = None
       self.connect()


   def __del__(self):
       self.disconnect()


   def connect(self):
       """Estabelece a conexão com o banco de dados MySQL."""
       try:
           self.connection = mysql.connector.connect(
               host=self.host,
               database=self.database,
               user=self.user,
               password=self.password,
               charset = 'utf8mb4'
           )
           if self.connection.is_connected():
               print('Conexão com o banco criada')
               return True
       except Error as e:
           print(f"Erro ao conectar ao MySQL: {e}")
           self.connection = None # Garante que a conexão seja None em caso de erro
           return False


   def disconnect(self):
       """Fecha a conexão com o banco de dados."""
       if self.connection and self.connection.is_connected():
           self.connection.close()
       print('Conexão liberada/destruída')




   def get_montadoras(self):
       """
       Retorna uma lista de dicionários com os dados da tabela tb_montadora.
       Cada dicionário representa uma linha da tabela.
       """
       if not self.connection or not self.connection.is_connected():
          return [] # Retorna lista vazia se a reconexão falhar


       records = []
       try:
           cursor = self.connection.cursor(dictionary=True) # Usar dictionary=True para retornar dicionários com os dados
           SQL = 'SELECT * FROM tb_montadora'
           cursor.execute(SQL)
           records = cursor.fetchall()
       except Error as e:
           print(f"Erro ao buscar dados de montadoras: {e}")
       finally:
           if 'cursor' in locals() and cursor: # Verifica se o cursor foi criado antes de fechar
               cursor.close()
       return records




# --- Teste de uso (smoke test) ---
if __name__ == "__main__":


   dao = MontadoraDAO()


   if dao.connection and dao.connection.is_connected():
       montadoras = dao.get_montadoras()


       if montadoras:
           print("\nDados das Montadoras:")
           for montadora in montadoras:
               print(montadora)
       else:
           print("Nenhuma montadora encontrada ou erro ao buscar dados.")
   else:
       print("Não foi possível estabelecer a conexão com o banco de dados.")

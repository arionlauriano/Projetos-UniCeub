import pandas as pd
import mysql.connector

#Não sei se o BD ta com um host ou nao mas qualquer coisa so me avisa e eu mudo

connection = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="Senha#",
    database="db_auto"
)


query = "SELECT * FROM compra;"  


df = pd.read_sql(query, connection)

connection.close()


df.to_excel("compra.xlsx", index=False)

print(" 'compra.xlsx' ta feito")

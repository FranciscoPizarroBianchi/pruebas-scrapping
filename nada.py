import mysql.connector
from mysql.connector import Error

try:
  cnx = mysql.connector.connect(
    host='localhost',
    port='3308',
    user='root',
    password='1234',
    db='taller'
  )
  if cnx.is_connected():
    print("Conexion exitosa.")
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO supermercado (nombreSupermercado) VALUES ('Santa Isabel')")
    cnx.commit()
    #resultados = cursor.fetchall()
    #for i in resultados:
    #  print(i[0])
except Error as ex:
  print("Error durante la conexion:",ex)
finally:
  if cnx.is_connected():
    cnx.close()
    print("La conexion ha finalizado.")
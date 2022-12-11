# importo el conector de mysql
import mysql.connector
# conecto a la base de datos
db = mysql.connector.connect(host="db4free.net", user="pruebascodo", passwd="Codo_2022", database="pruebascodo")
# creo el cursor
cursor = db.cursor()
#pido usuario y contraseña
nusuario=input("Ingrese el usuario: ")
contrasenia=input("Ingrese la contraseña: ")
#creo la consulta
sql = "SELECT * FROM usuarios WHERE username = %s AND pass = %s"
 #    "select * from usuarios where username='" + nusuario + "' and pass='" + contrasenia + "'"
#creo los valores para la consulta
valores=(nusuario, contrasenia)
cursor.execute(sql, valores)
#obtengo los resultados
resultados=cursor.fetchall()
# si hay resultados, el usuario y contraseña son correctos
if resultados:
    print("Bienvenido")
else:
    print("Usuario o contraseña incorrectos")
# cierro la conexion
db.close()


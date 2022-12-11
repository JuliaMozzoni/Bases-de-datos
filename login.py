#importamos el conector
import mysql.connector
#creamos la coneccion con el servidor
cnx=mysql.connector.connect(host='127.0.0.1', user='root', password='')
#crear un cursor
cursor=cnx.cursor()
#indicar con que base de datos trabajaremos
cursor.execute("USE carritophp")
#pedir usuario y contraseña
usuario=input("ingrese su nombre de usuario: ")
password=input("ingrese su contraseña: ")
#consultar la base de datos 
cursor.execute("select * FROM usuarios WHERE username='" + usuario + "' AND password='" + password + "'")
#cursor.execute("select * FROM usuarios WHERE username='alguien' AND password='mipas'")
cursor.fetchall()
#averiguar cuantos registros devuelve
print (cursor.rowcount)
if cursor.rowcount ==1:
    print("bienvenido!!")
else:
    print("usuario o contraseña incorrectos!")

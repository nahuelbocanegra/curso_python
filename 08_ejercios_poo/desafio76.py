
#  Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
#  base de datos MySQL:
#  - Host: mysql-5707.dinaserver.com
#  - Port: 3306
#  - User: mouredev_read
#  - Password: mouredev_pass
#  - Database: moure_test
#  Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
#   SELECT * FROM `challenges`
#   Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
 
import mysql.connector

conexion= mysql.connector.connect(
    host="mysql-5707.dinaserver.com",
    user="mouredev_read",
    port="3306",
    password="mouredev_pass",
    database="moure_test"
)

cursor=conexion.cursor()

cursor.execute("SELECT * FROM challenges")

resultado=cursor.fetchall()

for fila in resultado:
    print(fila)
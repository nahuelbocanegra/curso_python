#   Crea un programa que simule el mecanismo de participación:
#   - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#     participantes, mostrarlos, lanzar el sorteo o salir.
#   - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#   - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#     (Y no lo duplicarás)
#   - Si seleccionas mostrar los participantes, se listarán todos.
#   - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#     (Avisando de si lo has eliminado o el nombre no existe)
#   - Si seleccionas realizar el sorteo, elegirás una persona al azar
#     y se eliminará del listado.
#   - Si seleccionas salir, el programa finalizará.

from database import con
 


class Participacion:

    def __init__(self,conexion):
        self.con=conexion

    def añadir_participante(self,valor):
        sql="INSERT INTO usuario (nombre) VALUES (%s)"
        cursor=self.con.cursor()
        cursor.execute(sql,(valor,))
        self.con.commit()
        cursor.close()


    def eliminar_participante(self,id):
        sql=f"DELETE FROM usuario WHERE id_usuario = %s"
        cursor=self.con.cursor()
        cursor.execute(sql,(id,))
        self.con.commit()
        cursor.close()

    def mostrar_participante(self):
        sql="SELECT * FROM usuario"
        cursor=self.con.cursor()
        cursor.execute(sql)
        for usuario in cursor.fetchall():
            print(usuario[1])
        cursor.close()
        



class Sorteo:
    
    usuarios=Participacion(con)
    
    def lanzar_sorteo():
        pass



def inicio():
    print("añadir y borrar participantes, mostrarlos, lanzar el sorteo o salir")
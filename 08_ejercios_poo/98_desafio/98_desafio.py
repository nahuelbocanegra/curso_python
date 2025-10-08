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
import random
 


class Usuario:

    def __init__(self,conexion):
        self.con=conexion

    def añadir_participante(self,valor):



        sql="INSERT INTO usuario (nombre) VALUES (%s)"
        cursor=self.con.cursor()
        cursor.execute(sql,(valor,))
        self.con.commit()
        cursor.close()


    def eliminar_participante(self,nombre):
        sql=f"DELETE FROM usuario WHERE nombre = %s"
        cursor=self.con.cursor()
        cursor.execute(sql,(nombre,))
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
    


    usuarios=Usuario()
    
    def lanzar_sorteo(self):

      
        sql="SELECT * FROM usuario"
        cursor=con.cursor()
        cursor.execute(sql)
        lista=cursor.fetchall()
        if lista:
            ganador=random.choice(lista)
            print(f"el ganador es: {ganador[1]}")
            self.usuarios.eliminar_participante(ganador[1])
        else:
            print("no hay participantes")
        cursor.close()  



def inicio():

    usuario=Usuario(con)
    sorteo=Sorteo()

    while True:

        print("1- Mostrar participante")
        print("2- Añadir participante")
        print("3- Eliminar participante ")
        print("4- Sortear participante")
        print("5- Salir")
        
        opcion = int(input("elegir una opcion: "))

        if opcion == 1:
            usuario.mostrar_participante()
        if opcion == 2:
            try:
                nombre=input("ingrese el nombre del participante que quiere agregar: ")
                if nombre.strip():
                    usuario.añadir_participante(nombre)
                else:
                    print("Nombre inválido")
            except: 
                print("el nombre ya esta en la lista")
       
        if opcion == 3:

            try:
                nombre=input("ingrese el nombre del participante que quiere eliminar: ")
                if nombre.strip():
                    usuario.eliminar_participante(nombre)
                else:
                    print("Nombre inválido")
            except:
                print("el nombre no se encuentra en la lista")

        if opcion == 4:

            sorteo.lanzar_sorteo()

        if opcion == 5:
            break


if __name__== "__main__":
    inicio()
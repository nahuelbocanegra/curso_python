#  9. Registro de Estudiantes. Escribe un programa que permita registrar estudiantes en
#  un arreglo. Cada estudiante debe tener un nombre, una edad y una lista de
#  asignaturas en las que está inscrito. Implementa una clase Estudiante con los
#  atributos mencionados y métodos para agregar asignaturas, mostrar la información
#  del estudiante y calcular su promedio de calificaciones.

class Estudiante:
    def __init__(self,nombre,edad,asignaturas):
        self.nombre=nombre
        self.edad=edad
        self.asignaturas=asignaturas

    def agregar_asignaturas(self,asignaturas):
        nueva_asignatura=input("ingrese la nueva asignatura: ")
        nota=int(input("ingrese la nota del alumno: "))

        if nueva_asignatura in asignaturas:
            return "esta materia ya se encuentra en las asignaturas del alumno"
        asignaturas[nueva_asignatura]=nota
        

    def mostrar_datos_alumno(self):
        print("----- datos del alumno -----")
        print(f"nombre :{self.nombre}")
        print(f"edad: {self.edad}")
        print("asignaturas")
        for asignatura,nota in self.asignaturas.items():
            print(f"{asignatura}:{nota}")
    def calcular_promedio(self,asignaturas):
        promedio=0

        for notas in asignaturas.values():
            promedio+=notas

        return f"el promedio del alumno es de: {promedio/len(asignaturas)}"


def crear_nuevo_estudiante():
    asignaturas={}
    nombre_completo=input("ingrese el nombre completo del alumno: ")
    edad=int(input("ingrese la edad del estudiante: "))

    while True:

        asignatura=input("ingrese el nombre de la asignatura: ")
        nota=int(input("ingrese la nota de la asignatura: "))
        asignaturas[asignatura]=nota
        opcion=input("desea seguir cargando materias n/s: ").lower()
        if opcion == "n":
            break

    return {
        "nombre":nombre_completo,
        "edad":edad,
        "asignaturas":asignaturas
    }




def main():
    estudiantes=[]
    
    while True:
        print("1- agregar estudiante")
        print("2- agregar asignaturas")
        print("3- mostrar datos del estudiante")
        print("4- calcular promedio")
        print("5- mostrar estudiantes")
        print("6- salir")

        try:
            opcion=int(input("ingrese una opcion: "))
        except ValueError:
            print("valor incorrecto")

        if opcion == 1:
            
            datos=crear_nuevo_estudiante()
            estudiantes.append(datos)
            
            estudiante=Estudiante(datos["nombre"],datos["edad"],datos["asignaturas"])

        if estudiante:
            if opcion == 2:
                estudiante.agregar_asignaturas()
            if opcion == 3:
                estudiante.mostrar_datos_alumno()
            if opcion == 4:
                print(estudiante.calcular_promedio(datos["asignaturas"]))
            if opcion == 5:
                for estudiante in estudiantes:
                    print(estudiante)
            if opcion == 6:
             print("hasta pronto")
             break
        else:
            print("OPCION INCORRECTA")
            
        
if __name__ == "__main__":
    main()
# 1. Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
#  Construye los siguientes métodos para la clase:
#  a. Unconstructor, donde los datos pueden estar vacíos.
#  b. Los setters y getters para cada uno de los atributos. Hay que validar las
#  entradas de datos.
#  c. mostrar(): Muestra los datos de la persona.
#  d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
#  Además, crea en una aplicación de consola que permita al usuario crear un objeto
#  Persona y evaluar si es mayo o menor de edad..


class Persona:
    def __init__(self,nombre,edad,DNI):

        self.nombre= nombre
        self.edad=edad
        self.DNI=DNI

    def mostrar_datos(self):
        
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"DNI: {self.DNI}")

        
    def esMayorDeEdad(self):

        if self.edad >= 18:
            return  True
        
        return False



def main():

    persona=None

    while True:
        
        print("1- crear persona ")
        print("2- consultar si es mayor de edad ")
        print("3- mostrar datos")
        print("4- exit")
        opcion=int(input("ingrese una opcion: "))

        
        if opcion == 1:
            
            nombre=input("ingrese su nombre: ")
            edad=int(input("ingrese su edad: "))
            dni=int(input("ingrese su DNI: "))

            persona=Persona(nombre,edad,dni)

        if opcion == 2:
            if persona:
                es_mayor=persona.esMayorDeEdad()

                print("es mayor de edad" if es_mayor else "no es mayor de edad")
            else:
                print("primero ingrese los datos de la persona ")

        if opcion == 3:
            if persona:
                persona.mostrar_datos()
            else:
                print("primero ingrese los datos de la persona ")

    
        if opcion == 4:
             
            break



if "__main__" == __name__:
    main()
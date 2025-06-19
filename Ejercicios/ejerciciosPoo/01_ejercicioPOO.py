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

        self.nombre= nombre,
        self.edad=edad
        self.DNI=DNI

    def mostrar(self):
        
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"DNI: {self.DNI}")

        
    def esMayorDeEdad(self):

        if self.eddad >= 18:
            return  True
        
        return False




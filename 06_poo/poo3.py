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
    # self => hace referencia al obj 
    # init => constructor 

    def __init__(self,nombre,edad,Dni):
        self.nombre =nombre #propiedades
        self.edad  =edad 
        self.Dni = Dni

    def __str__(self):
        return f"{self.nombre},{self.edad},{self.Dni}"
    
    #metodos
    
    def mostrar(self):
        return f"{self.nombre},{self.edad},{self.Dni}"

persona1=Persona("nahu",23,40502975)
persona2=Persona("isma",32,36542345)

print(persona1.mostrar())
print(persona2.mostrar())

lista=[persona1,persona2]

print(lista)
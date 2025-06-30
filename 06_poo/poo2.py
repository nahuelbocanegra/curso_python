
#modularizacion => dividir un programa grande en módulos más pequeños y manejables
#encapsulacion =>  permite controlar el acceso a los atributos y métodos de una clase
#metodos de acceso => 
#herencia => nos permite definir una clase que hereda todos los métodos y propiedades de otra clase
    #La clase padre es la clase de la que se hereda, también llamada clase base
    # La clase hija es la clase que hereda de otra clase, también llamada clase derivada.


class Auto:  # modelo de caracteristicas comunes de un grupo de objetos

    #self => objeto perteneciente a la clase
    
    #__init__ => constructor =>  estado inicial de las clase

    #propiedades
    largoChasis=250
    anchiChasis=120
    ruedas=4
    enMarcha=False

    def __init__(self):
        #se llama automáticamente cada vez que se utiliza la clase para crear un nuevo objeto
        pass
    def __str__(self):
        # función controla lo que debe devolverse cuando el objeto de clase se representa como una cadena.
        return f"{self.largoChasis}({self.enMarcha})"
    #metodos

    def arrancar(self):
        self.enMarcha=True #cambiamos el valor de la propiedad del objeto 

    def frenar(self):
        pass #declaracion para evitar un error

auto=Auto() # instancia => ejemplar pertenecen a una clase


print(auto)
#POO

class Coche:

    #propiedades

    #init => estado inicial de un objeto (constructor)
    #enmarcha,ruedas,largo_chasis,ancho_chasis
    
    def __init__(self):
        
        self.__largo_chasis=250 #encapsular = necesitamos que no sea accesible desde fuera de la clase
        self.__ancho_chasis=120
        self.__ruedas=4
        self.__enmarcha=False

    #comportamiento(metodos)

    def arrancar(self,arrancamos): #self => hace referencia al propio abjeto de la clase
        self.enmarcha=arrancamos
        if self.enmarcha:
            return "el coche esta en marcha"
        
        return "el coche esta apagado"

      

    def estado(self):
        print(f"el coche tiene {self.__ruedas} ruedas , un ancho de {self.__ancho_chasis},y un largo de {self.__largo_chasis}")

        

# instanciar clase

coche1=Coche()
#metodo
print(coche1.arrancar(True))
coche1.estado()


print("segundo objeto")
coche2=Coche()
coche2.estado()
print(coche2.arrancar(False))

#encapsulacion => permite ocultar los detalles internos de un objeto 
# y exponer solo lo que es necesario para el resto del sistema  (ej = __ruedas)

# esto esta mal , nustro programa no deberia permitir esto
coche2.__ruedas=2 




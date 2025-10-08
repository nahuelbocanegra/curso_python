#las clases son plantillas para crear objetos.un objeto es una instancia de una clase
#nos permite agrupar datos (atributos) y funciones (metodos) en un solo lugar

class Coche():
    #atributo de clase(comparte toda las instancias)
    tipo="vehiculo de cuatro ruedas"

    #metodo especial que es el que construye el obj 
    # se llama aautomaticamente este metodo cuando creas la instancia
    def __init__(self,marca,color,modelo):

        #atributo de la instancia:
        self.marca=marca
        self.modelo=modelo
        self.color = color

    def arrancar(self):
        print(f"el auto {self.marca} {self.modelo} arrancó!")


micoche=Coche("toyota","rojo","t-14")
micoche.arrancar()

#encapsulacion: es ocultar los detalles internos de una clase y exponer solo la interfaz publica 
        
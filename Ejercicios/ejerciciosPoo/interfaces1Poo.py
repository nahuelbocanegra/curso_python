from abc import ABC,abstractmethod

#ABC => convierte una clase en una clase abstracta 

class Vehiculo(ABC): 
    #(ABC)=> HERENCIA   
    # clases abstractas => son plantillas que definen una estructura común para otras clases

    
    @abstractmethod
    def arrancar(self):
        return "Vehículo arrancado"
    @abstractmethod 
    def frenar(self):
        pass
    

class Auto(Vehiculo):

    def arrancar(self):
        return super().arrancar()

    def frenar(self):
        return super().frenar()

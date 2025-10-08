#  5. Kilometraje Recorrido. Crea una clase vehículo que permita llevar el kilometraje
#  recorrido. Agrega atributos para definir color, marca, modelo y patente del vehículo y
#  métodos para: 1- conducir el auto (debe aceptar la cantidad de kilómetros y sumarlo
#  al kilometraje recorrido) y 2- muestre en pantalla los datos del vehículo y el
#  correspondiente kilometraje. Además, escribe una aplicación de consola que permita 1
# al usuario conducir varios kilómetros y mostrar el kilometraje actual hasta que decida
#  detenerse. Al finalizar deberá mostrar los datos del vehículo y el kilometraje
#  recorrido.

class Vehiculo:
    def __init__(self,color,marca,modelo,patente):
         self.color=color
         self.marca=marca  
         self.modelo=modelo  
         self.patente=patente
         self.kilometraje=0

    def conducir_auto(self,km_recorridos):

        self.kilometraje+=km_recorridos

        return f"el nuevo kilometraje es {self.kilometraje}"
    
    def datos_autos(self):
        return f"""
        ----- datos del vehiculo -----
                {self.color}
                {self.marca}
                {self.modelo}  
                {self.patente}
                {self.kilometraje}

        """
    
def main():

    while True:

        print("1- Crear vehiculo")
        print("2- ver datos del vehiculo")
        print("3- conducir")
        print("4- Salir ")

        try:
            opcion=int(input("Ingresar una opcion: "))
        except ValueError:
            print("entrada invalida")
            continue

        if opcion == 1:

            try:
                
                color=input("Ingrese su nombre: ")
                marca=input("Ingrese su nombre: ")
                modelo=input("Ingrese su apellido: ")
                patente=input("Ingrese el numero de cuenta: ")

                auto=Vehiculo(color,marca,modelo,patente)
                print("vehiculo creado exitosamente")
            except ValueError:
                print("dato invalido")

        if auto:



            if opcion == 2:
                auto.datos_autos()
            if opcion == 3:
                while km_recorridos != 0:
                    km_recorridos=int(input("cuantos km recorrio / 0 para terminar de cargar"))
                    auto.conducir_auto(km_recorridos)

        if opcion == 4:
                break

if __name__ == "__main__":
    main()
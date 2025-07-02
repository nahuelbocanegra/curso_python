#  7. Expocoches. Escribe un programa de consola para gestionar la venta de entradas (no
#  numeradas) de Expocoches que tiene 3 zonas, la sala principal con 1000 entradas
#  disponibles, la zona de compra-venta con 200 entradas disponibles y la zona vip con
#  25 entradas disponibles. Hay que controlar que existen entradas antes de venderlas.
#  Define las clase Zona con sus atributos y métodos correspondientes y crea un
#  programa de consola que permita vender las entradas.
#  El menú del programa debe ser el siguiente: 1- Mostrar número de entradas libres,
#  2- Vender entradas y 3- Salir

class Voleteria:
    def __init__(self):
        self.principal=1000
        self.compra_venta=200
        self.vip=25

    def mostrar_entradas_disponibles(self):
        pass

    def vender_entradas(self):
        pass
    

def main():
    voleteria=Voleteria()
    while True:
        print("1 mostrar entradas disponibles")
        print("2 comprar entradas ")
        print("3 salir")
        
        try:
            opcion=int(input("ingrese un opcion"))
        except ValueError:
            print("valor erroneo ")

        if opcion == 1:
            voleteria.mostrar_entradas_disponibles()
        if opcion == 2:
            voleteria.vender_entradas()
        if opcion == 3:
            print("vuelva pronto")
            break

if __name__ == "__main__":
    main()
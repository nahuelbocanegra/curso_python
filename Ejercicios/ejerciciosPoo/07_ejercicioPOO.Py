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
        print(f"\nEntradas disponibles \nPrincipal: {self.principal}\nCompra-Venta: {self.compra_venta}\nVip: {self.vip}\n")

    def vender_entradas(self):
        while True:
            print("¿Que entrada desea comprar?")

            print("1 Entradas Principal")
            print("2 Compra y Venta ")
            print("3 VIP" )
            print("4 salir")
        
            try: 
                opcion=int(input("ingrese un opcion: "))
                cantidad=int(input("¿Cuantas entradas desea comprar?"))
            except ValueError:
                print("valor erroneo ")
                continue
           
            if opcion in [1,2,3]:
                self.__entradas(opcion,cantidad)
            if opcion == 4:
                break     
            else:
                print("opcion invalida")

           

    def __entradas(self,opcion,cantidad):
        tipos_entradas=[self.principal,self.compra_venta,self.vip]

       
        if tipos_entradas[opcion-1] <= 0 or tipos_entradas[opcion-1] < cantidad:
                
                return "no hay suficientes entradas"
                    
        tipos_entradas[opcion-1]-=cantidad     
      
           
        


   
def main():
    voleteria=Voleteria()
    while True:
        print("1 mostrar entradas disponibles")
        print("2 comprar entradas ")
        print("3 salir")
        
        try:
            opcion=int(input("ingrese un opcion: "))
        except ValueError:
            print("valor erroneo ")
            continue
            

        if opcion == 1:
            voleteria.mostrar_entradas_disponibles()
        elif opcion == 2:
            voleteria.vender_entradas()
        elif opcion == 3:
            print("vuelva pronto")
            break
        else:
            print("opcion invalida")

if __name__ == "__main__":
    main()
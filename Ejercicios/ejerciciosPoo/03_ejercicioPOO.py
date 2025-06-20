#  3. Producto. Crea una clase Producto con los siguientes atributos: Nombre, Precio y
#  Stock siendo obligatorios sólo los atributos Nombre y Precio. El Stock debe comenzar
#  con 0. Define métodos para actualizar el stock, para calcular el total del inventario y
#  para ver los datos. Además, escribe una aplicación de consola que permita al usuario:
#  1- actualizar el stock y 2- calcular inventario hasta que decida detenerse. Al finalizar
#  deberá mostrar los datos del producto, stock e inventario final.

class Producto:
    def __init__(self,nombre, precio ):
        self.nombre=nombre
        self.precio=precio
        self.stock=0

    def actualizar_stock(self,nuevo_stock):
        self.stock=nuevo_stock

    def calcular_inventario(self):
        inventario=self.stock*self.precio
        return f"el total del inventario es:{inventario}"

    def datos_producto(self):
        print(f"producto: {self.nombre}")
        print(f"stock: {self.stock}")
        print(f"precio: {self.precio}")


def main():
    producto=None

    while True:
        print("\n -------- MENU --------")
        print("1- crear producto")
        print("2- actualizar stock")
        print("3- calcular inventario")
        print("4- mostrar datos del producto")
        print("5- salir")

        try:
            opcion=int(input("ingresar una opcion: "))
        except ValueError:
            print("opcion invalida")
            continue

        if opcion == 1:
            nombre=input("ingrese el nombre del producto: ")
            precio=float(input("ingrese el precio del producto: "))
            producto=Producto(nombre,precio)
        if producto:
            if opcion == 2:
              
                nuevo_stock=int(input("ingrese el nuevo stock: "))
                producto.actualizar_stock(nuevo_stock)

            if opcion == 3:
                print(producto.calcular_inventario())

            if opcion == 4:
                producto.datos_producto()
        elif opcion == 5:
            break
      
        else:
            print("crea un producto")
if  __name__ == "__main__":
    main()()
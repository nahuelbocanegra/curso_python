#  8. Compra de Productos. Escribe un programa de consola para gestionar la compra de
#  productos. Cada producto se define por: id (autoincremental), nombre, caducidad y
#  precio que estará sujeto a la la fecha de caducidad como sigue:
#  ● Si le quedan entre 3 y5días, se reduce un 40%
#  ● Si le quedan menos de 3 dias, se reduce un 70%
#  ● No se podrán vender productos vencidos.

# from datetime import datetime, date, timedelta


# class Producto:
#     # hoy=date.today()
#     # contador_id=4

#     def __init__ (self,nuevo_producto,productos):


#         self.nombre=nuevo_producto["nombre"]  
#         self.caducidad=nuevo_producto["caducidad"]  
#         self.precio=nuevo_producto["precio"]  

#         producto={
#             "id":nuevo_producto["id"] ,
#             "nombre":nuevo_producto["nombre"] , 
#             "caducidad":nuevo_producto["caducidad"],
#             "precio":nuevo_producto["precio"]
#         }

#         productos.append(producto)

#     def mostrar_productos(self,productos):
#             for producto in productos:
#                 print(producto)




        
    # def eliminar_producto(self,id):
    #     for producto in Producto.productos:
    #        if producto["id"] == id:
    #             del producto

    # def actualizar_producto(self,id,datos):
    #     for producto in Producto.productos:
    #        if producto["id"] == id:
    #             producto["precio"]=datos




# def main():
#     carrito=[]    

#     while True:
#         print("1 ver productos disponibles")
#         print("2 agregar un producto al carrito")
#         print("3 salir")

#         try:
#             opcion=int(input("Elija una opcion: "))
#         except ValueError:
#             print("INGRSE UN VALOR CORRESPONDIENTE")


        
#         if opcion == 1:
#             pass
#         if opcion == 2:
#             pass
#         if opcion == 3:
#             break

"""Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta
de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar
los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta."""

def descuento(precio,descuento):
    return precio-(precio * descuento)

def aplicar_iva(producto,iva):
    return producto + (producto * iva/100)

def compras(productos,funcion_aplicar):
    total_compra=0
        
    for nombre,datos in productos.items():
    
        producto_precio=datos["precio"]
        producto_descuento=datos["descuento"]

    
        precio_descuento=descuento(producto_precio,producto_descuento)
        precio_final=funcion_aplicar(precio_descuento,20)
                                     
        total_compra+= precio_final
        print(f"{nombre} : {precio_final} ")
      
         
    print(f"el total de la compra es de:{total_compra}")

        

productos = {
    "manzana": {
        "precio": 10,
        "descuento": 0.10  # 10%
    },
    "banana": {
        "precio": 30,
        "descuento": 0.05  # 5%
    },
    "pan": {
        "precio": 120,
        "descuento": 0.15  # 15%
    },
    "leche": {
        "precio": 99,
        "descuento": 0.20  # 20%
    },
    "huevos": {
        "precio": 250,
        "descuento": 0.10  # 10%
    },
    "queso": {
        "precio": 375,
        "descuento": 0.25  # 25%
    },
    "café": {
        "precio": 420,
        "descuento": 0.30  # 30%
    }
}

compras(productos,aplicar_iva)

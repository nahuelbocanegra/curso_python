"""Tienes una lista de diccionarios, donde cada uno representa un producto con su nombre, 
categoría y puntuación de reseñas. Tu tarea es encontrar el producto 
con la mayor puntuación en cada categoría."""



productos = [
    {'nombre': 'Laptop A', 'categoria': 'Electrónica', 'puntuación': 4.5},
    {'nombre': 'Laptop B', 'categoria': 'Electrónica', 'puntuación': 4.7},
    {'nombre': 'Smartphone X', 'categoria': 'Electrónica', 'puntuación': 4.6},
    {'nombre': 'Cafetera', 'categoria': 'Hogar', 'puntuación': 4.3},
    {'nombre': 'Aspiradora', 'categoria': 'Hogar', 'puntuación': 4.8},
    {'nombre': 'Silla Gamer', 'categoria': 'Muebles', 'puntuación': 4.4},
    {'nombre': 'Escritorio', 'categoria': 'Muebles', 'puntuación': 4.1},
]




def mayor_puntuacion(productos):
    mejores_categorias={}
    categorias=set([categoria["categoria"] for categoria in productos])


    for categoria in categorias:
        mejores_categorias[categoria]= max(
        [p for p in productos if p["categoria"] == categoria],
        key=lambda x: x["puntuación"])

    return mejores_categorias
  

mayor_puntuacion(productos)


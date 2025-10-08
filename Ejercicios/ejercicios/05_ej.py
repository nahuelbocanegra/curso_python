"""Escribir una función que reciba una frase y 
devuelva un diccionario con las palabras que contiene y su longitud.
"""
text="Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud"
def contar_longitud(text):
    lista=text.split()
    dicc={}

    for palabra in lista:
        dicc[palabra]=len(palabra)

    return dicc

print(contar_longitud(text))
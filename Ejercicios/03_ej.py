"""
Escribir una función que reciba otra función
 y una lista, y devuelva otra lista con el resultado 
 de aplicar la función dada a cada uno de los elementos de la lista.
"""
def recibir_funcion(elemento):
    return elemento * elemento
lista=[1,2,3,4,5,6,7]

def funcion(recibir_funcion,lista):
    nueva_lista=[]
    for i in lista:
        nueva_lista.append(recibir_funcion(i))
    
    return nueva_lista

print(funcion(recibir_funcion,lista))


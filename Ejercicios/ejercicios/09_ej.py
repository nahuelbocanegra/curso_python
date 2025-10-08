""" Escribir un programa que encuentre el segundo número más grande en una lista
"""
lista=[111,121,32,44,25,364,17,28]
def sengundo_max(lista):
    maximo=max(lista)
    segundo_max=0
    for num in lista:
        if segundo_max<num and num < maximo:
            segundo_max= num 
           
    
    return segundo_max

print(sengundo_max(lista))
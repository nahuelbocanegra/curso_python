"""Escribir una función que reciba otra función booleana y una lista, 
y devuelva otra lista con los elementos de la lista que devuelvan 
True al aplicarles la función booleana."""


def fun_bool(num):
    
    if num % 2 == 0:
        return True
    return False


lista=[23,3,22,33,44,52,12,22,88]

def recibir_fun(fun_bool,lista):
    nueva_lista=[]
    for num in lista:
       if fun_bool(num):
           nueva_lista.append(num)
    return nueva_lista
           

print(recibir_fun(fun_bool,lista))

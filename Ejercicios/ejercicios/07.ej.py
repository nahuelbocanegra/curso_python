"""Crear un diccionario para contar la cantidad de veces que aparece cada carácter en
una cadena
"""

caracteres="Crear un diccionario para contar la cantidad de veces que aparece cada carácter en una cadena"

def contar_caracteres(caracteres):
    dicc_caracteres={}
    caracteres=caracteres.lower()
    for letra in caracteres:
        if letra == " ":
            continue

        if letra in dicc_caracteres:
             dicc_caracteres[letra]+=1
        else:
            dicc_caracteres[letra]=1
        
    return dicc_caracteres

print(contar_caracteres(caracteres))

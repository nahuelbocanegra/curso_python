#  Crea una función que encuentre todas las combinaciones de los números
#   de una lista que suman el valor objetivo.
#   - La función recibirá una lista de números enteros positivos
#     y un valor objetivo.
#   - Para obtener las combinaciones sólo se puede usar
#     una vez cada elemento de la lista (pero pueden existir
#     elementos repetidos en ella).
#   - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#     Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#     (Si no existen combinaciones, retornar una lista vacía)

def encontrar_combinaciones(lista_num,objetivo):
    
    combinaciones=[]

    for numero in lista_num :
        for numero2 in lista_num:
           if numero2 != numero:
                if numero+numero2 == objetivo:
                    if numero in combinaciones:
                        continue
               
                    combinaciones.append(numero)
                    combinaciones.append(numero2)
    
    return combinaciones
    
print(encontrar_combinaciones([1,2,3,4,5,6,7,8,9],14))
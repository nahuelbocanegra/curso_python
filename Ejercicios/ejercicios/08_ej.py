"""
Encontrar la suma de todos los números impares entre 1 y 50
"""

def suma_impares():
    suma_impar=0
    for num in range(0,50):
        if num % 2 != 0:
            suma_impar+=num

    return suma_impar

print(suma_impares())
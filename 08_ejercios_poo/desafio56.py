# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import random




caracteres=[[0,1,2,3,4,5,6,7,8,9],
    [chr(letra)for letra in range(ord("A"),ord("Z") + 1)],
    [chr(letra) for letra in range(ord("a"),ord("z") + 1)],
    list("!@#$%^&*()-_=+[]{};:'\",.<>/?|\\`~")
]

def generar_contraseña():
    cadena=""
    while True:
        try:
            cantidad=int(input("ingrese la cantidad de caracteres para su contraseña, entre 8 y 16: "))
        except ValueError:
            print("ingrese un numero del 8 al 16")
            continue
        if cantidad < 8 or cantidad > 16:
            print("la cantidad de caracteres tiene que ser menor a 16 y mayor que 8")
            continue


        for i in range(cantidad):
            random_tipo=random.randint(0,3)
            random_caracter=random.randint(0,len(caracteres[random_tipo])-1)
            caracter=caracteres[random_tipo][random_caracter]

            cadena+=str(caracter)

        break

    return cadena


print(f"Su contraseña es: {generar_contraseña()}") 




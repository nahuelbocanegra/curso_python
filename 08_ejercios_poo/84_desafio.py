# /*
#  * Crea una función que sea capaz de leer el número representado por el ábaco.
#  * - El ábaco se representa por un array con 7 elementos.
#  * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
#  *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
#  * - El primer elemento del array representa los millones, y el último las unidades.
#  * - El número en cada elemento se representa por las cuentas que están a
#  *   la izquierda del alambre.
#  *
#  * Ejemplo de array y resultado:
#  * ["O---OOOOOOOO",
#  *  "OOO---OOOOOO",
#  *  "---OOOOOOOOO",
#  *  "OO---OOOOOOO",
#  *  "OOOOOOO---OO",
#  *  "OOOOOOOOO---",
#  *  "---OOOOOOOOO"]
#  *
#  *  Resultado: 1.302.790
#  */

abaco=["O---OOOOOOOO",
   "OOO---OOOOOO",
   "---OOOOOOOOO",
   "OO---OOOOOOO",
   "OOOOOOO---OO",
   "OOOOOOOOO---",
   "---OOOOOOOOO"]


def convertir_abaco(abaco):

    numero_abaco=" "
    cantidad=0

    for digito in abaco:
        if digito[0] == "-":
            numero_abaco += "0"
            continue
        for numero in digito:

            if numero == "O":
                cantidad+=1
            if numero == "-":
                numero_abaco+=str(cantidad)
                cantidad=0
                break

    return int(numero_abaco)
                
  


convertir_abaco(abaco)
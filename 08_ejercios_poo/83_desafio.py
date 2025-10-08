#  * Los primeros dispositivos móviles tenían un teclado llamado T9
#  * con el que se podía escribir texto utilizando únicamente su
#  * teclado numérico (del 0 al 9).
#  *
#  * Crea una función que transforme las pulsaciones del T9 a su
#  * representación con letras.
#  * - Debes buscar cuál era su correspondencia original
#  * - Cada bloque de pulsaciones va separado por un guión.
#  * - Si un bloque tiene más de un número, debe ser siempre el mismo.
#  * - Ejemplo:
#  *     Entrada: 6-666-88-777-33-3-33-888
#  *     Salida: MOUREDEV
#

# Cada posición representa las letras de cada tecla
teclas = {
    "2": ["A","B","C"],
    "3": ["D","E","F"],
    "4": ["G","H","I"],
    "5": ["J","K","L"],
    "6": ["M","N","O"],
    "7": ["P","Q","R","S"],
    "8": ["T","U","V"],
    "9": ["W","X","Y","Z"]
}

def transcribir(numeros):

  mensaje=""
  numeros=numeros.split("-")
  for numero in numeros:
        mensaje+=teclas[numero[0]][len(numero)-1]

  return mensaje
        
       

print(transcribir("6-666-88-777-33-3-33-888"))
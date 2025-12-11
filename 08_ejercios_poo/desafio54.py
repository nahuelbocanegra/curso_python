#
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  


leet = {
    "A": "4",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "|=",
    "G": "6",
    "H": "#",
    "I": "1",
    "J": "_|",
    "K": "|<",
    "L": "1_",
    "M": "/\\/\\",
    "N": "/\\/",
    "O": "0",
    "P": "|*",
    "Q": "0_",
    "R": "|2",
    "S": "5",
    "T": "7",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "><",
    "Y": "`/",
    "Z": "2"
} 

def tradicir_leet(lett,txt):

    mensaje=[]

         
    for i in txt.upper():

        if i in lett:

        
           mensaje.append(lett[i])
            
        
    return "".join(mensaje)

print(tradicir_leet(leet,"hola"))
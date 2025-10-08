# /*
#  * Crea las funciones capaces de transformar colores HEX
#  * a RGB y viceversa.
#  * Ejemplos:
#  * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#  * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#  */


def cambioRGB(hex):
    
    if len(hex) != 7:
        return "no es un numero hex"
    
    hex=hex.lstrip("#")


    for caracter in hex:
        
        if caracter.upper() not in "ABCDEF0123456789":
        
                return "No es un caracter hex"
    

    convertir(hex)
   
def convertir(hex):
        
    r=int(hex[0:2],16)
    g=int(hex[2:4],16)
    b=int(hex[4:6],16)

    rgb=(r,g,b)

    print(rgb)


cambioRGB("#00A0B0")
#   Crea una función que sea capaz de transformar Español al lenguaje básico
#   del universo Star Wars: el "Aurebesh".
#   - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#   - También tiene que ser capaz de traducir en sentido contrario.
#  
#   ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  
#   ¡Que la fuerza os acompañe!



aurebesh = {
    "A": "Aurek", "B": "Besh", "C": "Cresh", "D": "Dorn", "E": "Enth",
    "F": "Forn", "G": "Grek", "H": "Herf", "I": "Isk", "J": "Jenth",
    "K": "Krill", "L": "Leth", "M": "Mern", "N": "Nern", "O": "Osk",
    "P": "Peth", "Q": "Qek", "R": "Resh", "S": "Senth", "T": "Trill",
    "U": "Usk", "V": "Vev", "W": "Wesk", "X": "Xen", "Y": "Yirt", "Z": "Zerek"
}

def traducir_espanol_aurebesh(mensaje):

    traduccion=" "

    for letra in mensaje:
        
        if  letra.upper() in aurebesh:
            traduccion += aurebesh[letra.upper()] + " "
      

    return traduccion


def traducir_aurebesh_espanol(mensaje):
    mensaje=mensaje.split(" ")
    traduccion=" "

    for palabra in mensaje:

        for key,valor in aurebesh.items():
            
            if palabra== valor:

                traduccion+=key + " "


    return traduccion


print(traducir_espanol_aurebesh("Herf Osk Leth Aurek "))

def main():

    while True:

        print("""
                1 - Traducir de Español a Aurebesh
                2 - Traducir de Aurebesh a Español
                3 - Salir
                """)
        
        try:
            opcion=int(input("elegir una opcion: "))
        except ValueError:
            print("error de valor")
            continue


        if opcion == 1:    
            mensaje=input("Que mensaje quieres traducir a aurebesh?: ")
            print(f"el mensaje es: {traducir_espanol_aurebesh(mensaje)}")
           

            

        if opcion == 2:
            mensaje=input("Que mensaje quieres traducir a español?: ")
            print(f"el mensaje es: {traducir_aurebesh_espanol(mensaje)}")
        
        if opcion == 3:
            break
        
        
if __name__ == "__main__":
    main()
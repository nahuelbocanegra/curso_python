# 6. Control de Volúmen. Crea una clase ControlVolumen que permita establecer el
#  volumen de un parlante (1 mínimo volumen, 10 máximo volumen). El constructor
#  establecerá el volumen en un nivel medio. Agrega métodos para: 1- ajustar el
#  volumen permitiendo que el mismo sume o reste sin salirse de los límites y 2
# mostrar el nivel de volúmen actual. Además, escribe una aplicación de consola que
#  permita al usuario manipular y consultar el volumen hasta que decida salir. Al
#  finalizar deberá mostrar el nivel actual de volumen.

class ControlVolumen:
    def __init__(self):
        self.volumen=5

    def mostrar_volumen(self):
       return  self.volumen
    
    def subir_volumen(self):
        if self.volumen >= 10:
            return "volumen al maximo"
        self.volumen+=1
        print(f"volumen: {self.volumen}")
    

    def bajar_volumen(self):
        if self.volumen <= 1:
            return "volumen al minimo"
        self.volumen-=1
        print(f"volumen: {self.volumen}")

def main():
    control=ControlVolumen()
    while True:

        print("1- consultar volumen ")
        print("2- bajar volumen ")
        print("3- subir volumen ")
        print("4- salir ")

        try:
            opcion=int(input("ingrese una opcion:"))
        except ValueError:
            print("valor incorrecto")
            continue

        if opcion == 1:
            control.mostrar_volumen()
        elif opcion == 2:
            control.bajar_volumen()
        elif opcion == 3:
            control.subir_volumen()
          
        elif opcion == 4:
            print(f"volumen: {control.mostrar_volumen()}")
            break
        else:
            print("opcion invalida")


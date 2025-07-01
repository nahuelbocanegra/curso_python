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
    
    def subir(self):
        if self.volumen >= 10:
            return "volumen al maximo"
        self.volumen+=1
    

    def bajar(self):
        if self.volumen <= 1:
            return "volumen al minimo"
        self.volumen-=1
    


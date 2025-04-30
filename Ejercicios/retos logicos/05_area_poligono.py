# Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.

class Poligono:


    def triandulo(base,altura):
        return (base*altura)/2
    
    def cuadrado(lado):
        return lado*lado
    
    def rectangulo(base,altura):
        return base*altura
    

def calcular(poligono):
    
    if poligono.lower() == "triangulo":
        base= int(input("ingrese la base del triangulo: "))
        altura= int(input("ingrese la altura del triangulo: "))

        return Poligono.triandulo(base,altura)
    
    if poligono.lower() == "cuadrado":
        lado=int(input("ingrese el lado del cuadrado: "))
        return  Poligono.cuadrado(lado)
    
    if poligono.lower() == "rectangulo":
        base=int(input("ingrese la base del triangulo: "))
        altura=int(input("ingrese la altura del triangulo: "))
        return  Poligono.rectangulo(base,altura)

    
print(calcular("cuadrado"))
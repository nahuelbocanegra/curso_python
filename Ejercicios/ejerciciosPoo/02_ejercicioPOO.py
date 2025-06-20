# 2. Área y Perímetro. Crea una clase Rectángulo que permita calcular su área y su
#  perímetro. Además, crea en una aplicación de consola que permita al usuario crear
#  un objeto Perímetro y realizar los cálculos. .


class Rectangulo:

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def perimetro(self):
        perimetro=2*(self.base+self.altura)
        return f"el perimetro del rectangulo es {perimetro}"

    def area(self):
        area=self.base *self.altura
        return f"el area del rectangulo es {area}"
    

def main():

    rectangulo=None
    while True:


        print("1- crear un rectangulo")
        print("2- Calcular el area del rectangulo")
        print("3- Calcular el perimetro del rectangulo")
        print("4- exit")

        try:
            opcion=int(input("ingresar una opcion: "))
        except ValueError:
            print("por favor,ingrese un numero valido")
            continue


        if opcion ==1:
            try:
                base=float(input("ingrese la base del rectangulo: "))
                altura=float(input("ingrese la altura del rectangulo: "))
                rectangulo=Rectangulo(base,altura)
                print("rectangulo creado exitosamente")
            except ValueError:
                print("valor incorrecto")
        elif opcion ==2:
            if rectangulo:
                print(rectangulo.area())
        elif opcion ==3:
            if rectangulo:
                print(rectangulo.perimetro())
        elif opcion ==4:
            print("chau")
        else:
            print("opcion invalida")
        

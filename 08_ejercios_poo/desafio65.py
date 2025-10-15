# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */
from datetime import date
import unittest


def buscar_viernes_trece(ano,mes):

    fecha=date(ano,mes,13)
    numero_dia=fecha.weekday()

    dias_semana={
        "lunes":0,
        "martes":1,
        "miercoles":2,
        "jueves":3,
        "viernes":4,
        "sabado":5,
        "domingo":6,
    }

    for dias,numero in dias_semana.items():

        if numero_dia == 4:
            print("es viernes 13")
        
        if numero_dia == numero:

            return dias


def main():

    while True:

        print("-1 Buscar viernes 13")
        print("-2 Exit")

        try:
            opcion=input("elige una opcion: ")
        except ValueError:
            print("opcion invalida")
            continue
        
        if opcion == 1:

            try:
                mes=int(input("Ingrese el mes que va a consultar: "))
                ano=int(input("Ingrese el ano que va a consultar: "))
                
            except ValueError:
                print("valor incorrecto, intente nuevamente")
                continue
            if not (1 >= mes <= 12):
                raise ValueError("el numero debe ser mayor o igual a 1 y menor o igual a 12")
            if not (ano >= 0):
                raise ValueError("el numero debe ser mayor o igual a 0")
            
        if opcion == 2:

            print("chau")
            break
    

class TestViernesTrece(unittest.TestCase):

    def test_buscar_viernes(self):
        self.assertEqual(buscar_viernes_trece(2025,10), "lunes")
        self.assertEqual(buscar_viernes_trece(1997,2), "jueves")
        self.assertEqual(buscar_viernes_trece(1993,1), "miercoles")


if __name__ == "__main__":

    unittest.main()
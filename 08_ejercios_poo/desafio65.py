# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */
from datetime import date


def buscar_viernes_trece(ano,mes):

    fecha=date(ano,mes,13)
    numero_dia=fecha.weekday()

    if numero_dia == 4:
        print("es viernes 13")
        




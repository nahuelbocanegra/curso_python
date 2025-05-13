# 5- CuandolaTierra completa una órbita alrededor del Sol, no han transcurrido
#  exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la
#  diferencia es de más o menos uncuarto de día.
#  Para evitar que las estaciones se desfasen con el calendario, el calendario juliano
#  introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados
#  bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.
#  Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente
#  3/400 de día.
#  Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo
#  calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que
#  fuera divisible por 400.
#  Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era
#  el calendario vigente en ese año



def es_bisiesto(anio):
    if anio < 1582:
        # Calendario juliano
        return anio % 4 == 0
    else:
        # Calendario gregoriano
        if anio % 4 != 0:
            return False
        elif anio % 100 != 0:
            return True
        elif anio % 400 == 0:
            return True
        else:
            return False

anio = int(input("Ingrese un año: "))

if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
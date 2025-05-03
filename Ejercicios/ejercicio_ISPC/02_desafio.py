#  2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
#  entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

"""hora_actual=input("ingresar la hora actual (h:m:s) : ")
entero_horas=input("ingrese un numero de horas: ")
"""
def hora(hora_actual,entero_horas):

    hora_actual= hora_actual.split(":")
    hora=int(hora_actual[0])
    minutos=int(hora_actual[1])
    segundos=int(hora_actual[1])

    print(hora,minutos,segundos)



hora("22:01:10",11)

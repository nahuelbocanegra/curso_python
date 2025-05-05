#  2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
#  entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

"""hora_actual=input("ingresar la hora actual (h:m:s) : ")
entero_horas=input("ingrese un numero de horas: ")
"""
def hora(hora_actual,entero_horas):


    hora=[int(h) for int(h) in hora_actual]

    print(hora)


   
    
   
    if hora > 24:
         hora_actual[0] = int(hora_actual[0]) - 24
    else:
        
         print(hora_actual)

    print(hora_actual)
        







hora("22:01:10",11)

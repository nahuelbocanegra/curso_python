#  4- Tiempodeviaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
#  tiene la duración en minutos de cada uno de los tramos del viaje.
#  Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
#  entregue como resultado el tiempo total de viaje en formato horas:minutos.
#  El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

def tiempo_de_viaje():
    tiempo_total=0
    
    while True:
        
        tramo=input("ingresar el tiempo por tramo en minutos, ingrese 0 para finalizar : ")
       
        if int(tramo) == 0:
            break
        if tramo.isnumeric():
            tiempo_total+=int(tramo)

    
    horas=tiempo_total//60
    minutos= tiempo_total-horas*60

    
    return f"tiempo total del viaje {horas}hs:{minutos}m"

print(tiempo_de_viaje())
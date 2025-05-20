# 12- TorneodeTenis. Escriba un programa para simular un campeonato de tenis.
#  Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
#  debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El
#  ganador de cadapartido avanza a la ronda siguiente.
#  El programa debe continuar preguntando ganadores de partidos hasta que quede un
#  único jugador, que es el campeón del torneo.

def torneoTenis():
    jugadores=inscripciones()
    index=0
    while True:
        ganador=input(f"Quie gana entre a- {jugadores[index]} vs b- {jugadores[index+1]} : ").lower()
        
        if ganador== "a":
            jugadores.remove(jugadores[index])
            index+=1
        if ganador== "b":
            jugadores.remove(jugadores[index+1])
            index+=1


        if len(jugadores) == 4:
            print("semifinal")
            index = 0
        if len(jugadores) == 2:
            print("final")
            index = 0
        if len(jugadores) == 1:
            print(f"el ganador es {jugadores[0]}")
            break

        print(jugadores)



def inscripciones():

    jugadores=[]

    for i in range(1,9):
        jugador=input(f"Nombre del jugador {i} : ")
        jugadores.append(jugador)

    return jugadores


torneoTenis()
#  11- Piedra, papelytijera.En cada ronda del juego del cachipún, los dos competidores
#  deben elegir entre jugar tijera, papel o piedra.
#  Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
#  piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
#  El ganador del juego es el primero que gane tres rondas.
#  Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
#  marcador después de cadaronda, y termine cuando uno de ellos haya ganado tres
#  rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra.


def jugar_piedra_papel_tijeras():    
    punto_j1=0
    punto_j2=0

    while True:
     

        jugador1=input("Jugador 1 : ingrese su jugada(piedra,papel,tijera): ").lower()
        jugador2=input("Jugador 2 : ingrese su jugada(piedra,papel,tijera): ").lower()

        if jugador2 in ["piedra","papel","tijera"] and jugador1 in ["piedra","papel","tijera"]:

            if jugador1 == jugador2:
                print("empate")
            elif jugador1 == "piedra" and jugador2 == "tijera" or \
                jugador1 == "papel" and jugador2 == "piedra" or\
                jugador1 == "tijera" and jugador2 == "papel" :

                    print("gana el jugador 1")
                    punto_j1+=1
            else:
                print("gana el jugador 2")
                punto_j2+=1

            if punto_j1 >= 3:
                print("¡Jugador 1 gana la partida!")
                break
            elif punto_j2 >= 3:
                print("¡Jugador 2 gana la partida!")
                break
        else:
            print("Entrada invalida,Ingrese (piedra papel o tijera) por favor")

jugar_piedra_papel_tijeras()


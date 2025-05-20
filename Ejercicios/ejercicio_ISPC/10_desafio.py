#  10- TorreyAlfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
#  numeradas de1 a8.Dosdelaspiezas del juego de ajedrez son el alfil y la torre. El alfil se
#  desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
#  pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
#  desplazarse:
#  Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
#  una torre, e indique cuál pieza captura a la otra

def ajedrez():

    torre_fila=int(input("Ingrese la fila de la torre: "))
    alfil_fila=int(input("Ingrese la fila de la alfil: "))
    torre_columna=int(input("Ingrese la columna de la torre: "))
    alfil_columna=int(input("Ingrese la columna de la alfil: "))


    for fila in range(1,9):
        for columna in range(1,9):
           
                print( f"{ fila*columna }",end=" ")

        print("\n")
    
    if  torre_columna == alfil_columna or torre_fila == alfil_fila: 
        print("torre gana")
    


ajedrez()


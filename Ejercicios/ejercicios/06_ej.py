"""Escribir una función reciba una lista de notas 
y devuelva la lista de calificaciones correspondientes a esas notas."""

def calificaciones(score):

    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'
    

def boletin(lista):
  
    for score in lista:
       cali =   calificaciones(score)
       print(f"{score} : {cali}")

lista=[1,2,10,9,6]
boletin(lista)
#  14- Signozodiacal. El signo zodiacal de una persona está determinado por su día de
#  El diccionario de signos asocia a cada signo el período del año que le corresponde. Cada
#  período es una tupla con la fecha de inicio y la fecha de término, y cada fecha es una
# tupla


def zodiaco(dia,mes):
    
    signos_zodiaco = {
        "Aries":       ((3, 21), (4, 19)),
        "Tauro":       ((4, 20), (5, 20)),
        "Géminis":     ((5, 21), (6, 20)),
        "Cáncer":      ((6, 21), (7, 22)),
        "Leo":         ((7, 23), (8, 22)),
        "Virgo":       ((8, 23), (9, 22)),
        "Libra":       ((9, 23), (10, 22)),
        "Escorpio":    ((10, 23), (11, 21)),
        "Sagitario":   ((11, 22), (12, 21)),
        "Capricornio": ((12, 22), (1, 19)),
        "Acuario":     ((1, 20), (2, 18)),
        "Piscis":      ((2, 19), (3, 20))
    }

    for signo,((mes_ini,dia_ini),(mes_fin,dia_fin)) in signos_zodiaco.items():
        if (mes_ini == mes and dia >= dia_ini) or (mes_fin == mes and dia <= mes_fin ):
            return signo
          

zodiaco(30,11)
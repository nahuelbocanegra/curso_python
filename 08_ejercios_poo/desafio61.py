#  Crea un generador de números pseudoaleatorios entre 0 y 100.
#  - No puedes usar ninguna función "random" (o semejante) del
#    lenguaje de programación seleccionado.
# 
#  Es más complicado de lo que parece...

import time

def  numeros_aleatorios():

    while True:
        segundos=time.time()
        num=int((segundos %1)*1000)
        yield num

gen=numeros_aleatorios()

for _ in range(10):
    print(next(gen))
    time.sleep(0.1)




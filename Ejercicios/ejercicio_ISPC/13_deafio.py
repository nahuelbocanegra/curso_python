# 13- El diccionario países asocia cada persona con el conjunto de los países que ha
#  visitado:
#  Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han
#  visitado la persona a y la persona b:8

def cuantos_en_comun(a, b):

    paises = {

        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},

    }

    paises_en_comun=0

    for i in paises[a]:
        if i in paises[b]:
            paises_en_comun+=1
        
    print(paises_en_comun)

    
        


cuantos_en_comun( 'Yayita','John')



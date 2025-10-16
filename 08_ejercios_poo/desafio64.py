#  Dada una URL con parámetros, crea una función que obtenga sus valores.
#  No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# 
#  Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  los parámetros serían ["2023", "0"]

def encontrar_parametros(url):

    url=url.split("?")
    url=url[1].split("&")

    parametros=[]

    for p in url:
        if "=" in p:
            clave,valor= p.split("=",1)

            parametros.append(valor)

    print(parametros)


  
   

encontrar_parametros("https://retosdeprogramacion.com?year=2023&challenge=0&hola2=perro")
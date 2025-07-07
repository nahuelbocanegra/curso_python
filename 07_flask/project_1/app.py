from flask import Flask,render_template

app=Flask(__name__)

@app.route("/") #ruta raiz
def inicio():
    return "Hola desde flask V2.0"

#direccion ip loopback 
    # direccion especial que se utiliza para 
    # comunicarse con el mismo dispositivo de red 
    # en que se orgina la comunicacion

#SET FLASK_DEBUG=True => SE VA RECARGAR CON CADA CAMBIO QUE HAGAS
#VARIABLE DE ENTORNO

@app.route("/saludar/<nombre>") #<nombre> parametro
def saludar(nombre):
    return f"hola {nombre}"

@app.route("/edad/<int:edad>")
def edad(edad):
    return f"{edad + 5}"


@app.route("/mostrar/<nombre>")
def mostrar(nombre):
    return render_template("mostrar.html",valor=nombre) #retornando un archivo html 




if __name__ == "__main__":
    app.run(debug=True)
    
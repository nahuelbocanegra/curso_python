from flask import Flask,render_template,redirect,url_for,abort

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

#redireccion de rutas

@app.route("/redireccion")
def redireccion():#codifgo 302
    #redirect => funcion de redireccion 
    return redirect(url_for("inicio")) #url_for se usa para generar URLs dinámicas basadas en el nombre de la vista(funcion)


#manejo de errores
#404 no existe la pag
#abort => indica a flask funcion que  error se va a mostrar

@app.route("/error")
def error():
    return abort(404)

@app.errorhandler(404) # decorador que recibe errores 
def pagina_no_found(error):
    return render_template("404.html",error=error),404 #por defecto el render_tempate te devuelve un codigo 200 




if __name__ == "__main__":
    app.run(debug=True)
    
from flask import Flask,render_template,redirect,url_for,abort,session,request

app=Flask(__name__)
#python -c import secrets; print(secrets.token_hex()) libreria de python para generar secret_key
app.secret_key="7f326bae76f522e71271808ede08d217b9ee7238603102d74d294ca8d9e2308b"


@app.route("/") #ruta raiz
def inicio():
    
    #sessions => es un diccionario que almacena datos para cada usuario conectado en web


    if "username" in session:
        return f"usuario incio sesion {session['username']}"
    return "no sesion"



@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("inicio"))
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("username",None) #cerrar sesion
    return redirect(url_for("inicio"))
#direccion ip loopback 
    # direccion especial que se utiliza para 
    # comunicarse con el mismo dispositivo de red 
    # en que se orgina la comunicacion

#SET FLASK_DEBUG=True => SE VA RECARGAR CON CADA CAMBIO QUE HAGAS
#VARIABLE DE ENTORNO

#diferentes rutas pueden contener la misma funcion
@app.route("/hola/<nombre>") 
@app.route("/saludar/<nombre>") #<nombre> parametro
def saludar(nombre):
    return f"hola {nombre}"

@app.route("/edad/<int:edad>")
def edad(edad):
    return f"{edad + 5}"


@app.route("/mostrar/<nombre>")
def mostrar(nombre):
    return render_template("mostrar.html",valor=nombre) #retornando un archivo html 


@app.route("/datos/<valor>", methods=["GET","POST"]) #estos metodos estan aceptados en esta ruta [GET,POST]
def mostrar_datos(valor):
    return f"Datos recibido: {valor} "

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
    
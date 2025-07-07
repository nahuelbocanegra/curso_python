from flask import Flask
from markupsafe import escape

#Flask => microframework


app = Flask(__name__) #instancia de clase 

#__name__ es el nombre del modulo o app 

@app.route("/") # route() indica que url activa la funcion
def hola_mundo():
    return "<p> hola mundo </p>"

@app.route("/<name>") #ruta con parametro
def hello(name):
    return f"Hello,{escape(name)}!" #La función escape se usa para proteger tu aplicación web contra ataques XSS (Cross-Site Scripting)
    
#reglas de variables
#  puedes usar un conversor para especificar el tipo de argumento
        #<converter:variable_name>

@app.route("/post/<int:post_id>")
def user_profile(username):
    return f"User {escape(username)}"


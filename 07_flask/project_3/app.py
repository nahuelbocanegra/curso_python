from flask import Flask ,render_template ,request ,url_for, redirect
from variables_entorno import DB_NAME,USER_NAME,SERVER_NAME,USER_PASSWORD,SECRET_KEY
from form import MensajeForm
from models import Mensaje
from database import db
from flask_migrate import Migrate



app=Flask(__name__)

#conectando base de datos con alchemy
FULL_URL_DB=f"mysql+pymysql://{USER_NAME}:{USER_PASSWORD}@{SERVER_NAME}/{DB_NAME}"

app.config['SQLALCHEMY_DATABASE_URI' ]=FULL_URL_DB

#sirve para intregrar una base de datos con flask
db.init_app(app)#sto vincula tu aplicación Flask (app) con la instancia de SQLAlchemy (db),
migrate=Migrate(app,db)#activa Flask-Migrate, una extensión que permite manejar las migraciones de base de datos de forma automática

app.config["SECRET_KEY"]=SECRET_KEY

@app.route("/")
def inicio():
    mensajes=Mensaje.query.all()
    return render_template("index.html",datos=mensajes)

@app.route("/mensaje",methods=["GET","POST"])
def insertar_mensaje():
    mensaje=Mensaje()
    mensajeForm=MensajeForm(obj=mensaje)

    if request.method=="POST":
        if mensajeForm.validate_on_submit():#se usa para verificar dos cosas al mismo tiempo , la solicitud es post, todos los campos pasaton la validacion
            mensajeForm.populate_obj(mensaje)
            db.session.add(mensaje)
            db.session.commit()
            return redirect(url_for("inicio"))

    return render_template("mensaje.html",formulario=mensajeForm)



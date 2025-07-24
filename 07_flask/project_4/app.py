from flask import Flask,render_template,url_for,request
from db import db
from variables_entorno import NAME_BASE,NAME_USER,SERVER_NAME,SECRET_KEY,USER_PASSSWORD
from flask_migrate import Migrate
from models import Contacto
from forms import NuevoContacto
app=Flask(__name__)

FULL_URL_DB=f"mysql+pymysql://{NAME_USER}:{USER_PASSSWORD}@{SERVER_NAME}/{NAME_BASE}"


app.config["SQLALCHEMY_DATABASE_URI"]=FULL_URL_DB

app.config["SECRET_KEY"]=SECRET_KEY


db.init_app(app)
migrate=Migrate(app,db)


@app.route("/")
def inicio():
    contactos=Contacto.query.all()
    return render_template("index.html",contactos=contactos)

@app.route("/nuevo_contacto",methods=["GET","POST"])
def insertar_contacto():

    contacto=Contacto()
    formulario_contacto=NuevoContacto(obj=contacto)

    if request.method == "POST":
        if formulario_contacto.validate_on_submit():
            formulario_contacto.populate_obj(contacto)
            db.session.add(contacto)
            db.session.commit()
            return render_template(url_for("inicio"))
    
    return render_template("insertar_contactos.html",formulario=formulario_contacto)

@app.route("/contacto/<int:id>")
def detalle_contacto(id):
    contacto=Contacto.query.get(id)
    return render_template("detalles_contacto.html",dato=contacto)




if __name__ == "__main__":
    app.run(debug=True)
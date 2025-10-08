from flask import Flask,render_template,url_for,request,redirect
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
            return redirect(url_for("inicio"))
    
    return render_template("insertar_contactos.html",formulario=formulario_contacto)

@app.route("/contacto/<int:id>")
def detalle_contacto(id):
    contacto=Contacto.query.get(id)
    return render_template("detalles_contacto.html",dato=contacto)

@app.route("/editar_contacto/<int:id>",methods=["GET","POST"])
def editar_curso(id):
    contacto=Contacto.query.get_or_404(id) #Busca en la base de datos un contacto con el ID pasado por la URL.
    contacto_form=NuevoContacto(obj=contacto)

    if request.method == "POST": #Verifica si el usuario envió el formulario
        if contacto_form.validate_on_submit(): #Valida que el formulario esté bien completado 
            contacto_form.populate_obj(contacto) #Copia los datos del formulario hacia el objeto contacto 
            db.session.commit() #Guarda los cambios en la base de datos.
            return redirect(url_for("inicio"))
        
    return render_template("editar_contacto.html",formulario=contacto_form)  #Si la petición no fue POST (es decir, fue GET), 
                                                                             #simplemente muestra el formulario con los datos ya cargados para editar.


@app.route("/eliminar_contacto/<int:id>",methods=["POST"])
def eliminar_contacto(id):
    contacto=Contacto.query.get_or_404(id)
    db.session.delete(contacto)
    db.session.commit()
    return redirect(url_for("inicio"))
    



if __name__ == "__main__":
    app.run(debug=True)
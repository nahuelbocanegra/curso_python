from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from variable_entorno import USER_DB,USER_PASSWORD,SERVER_DB,NAME_DB
from models import Cursos
from database import db

app=Flask(__name__)

#conctando base de datos con alchemy

FULL_URL_DB=f"mysql+pymysql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}"

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB


#migrar el modelo

db.init_app(app)
migrate=Migrate(app,db)



@app.route("/")
def inicio():
    cursos=Cursos.query.all()
    total_cursos=Cursos.query.count()

    
    return render_template("index.html",total=total_cursos,datos=cursos)

@app.route("/curso/<int:id>")
def ver_curso(id):
    curso=Cursos.query.get(id) #buscar el registro en la base de datos
    return render_template("cursos_detalle.html",dato=curso)

@app.route("/insertar_curso",methods=["GET","POST"])
def insertar_curso():
    pass 


if __name__ == "__main__":
    app.run(debug=True)


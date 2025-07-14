from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String
from flask_migrate import Migrate
from variable_entorno import USER_DB,USER_PASSWORD,SERVER_DB,NAME_DB

app=Flask(__name__)

#conctando base de datos con alchemy

FULL_URL_DB=f"mysql+pymysql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}"

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB

db=SQLAlchemy(app)

#migrar el modelo

migrate=Migrate()
migrate.init_app(app,db)

#modelo de datos

class Cursos(db.Model):
    id: Mapped[int]=mapped_column(String(100),primary_key=True)
    nombre:Mapped[str]=mapped_column(String(100),unique=True)
    instructor:Mapped[str]=mapped_column(String(100))
    topico:Mapped[str]=mapped_column(String(100))

    def __str__(self):
        return f"""
            id:{self.id}
            nombre:{self.nombre}
            instructor:{self.instructor}
            topico:{self.topico}
        """

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def inicio():
    cursos=Cursos.query.all()
    total_cursos=Cursos.query.count()

    
    return render_template("index.html",total=total_cursos,datos=cursos)

@app.route("/curso/<int:id>")
def ver_curso(id):
    curso=Cursos.query.get(id) #buscar el registro en la base de datos
    return render_template("cursos_detalle.html",dato=curso)

@app.route("/insertar_curso",["GET","POST"])
def insertar_curso():
    pass 
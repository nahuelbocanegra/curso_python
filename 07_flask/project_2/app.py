from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped,mapped_column
from flask_migrate import Migrate
from variable_entorno import USER_DB,USER_PASSWORD,SERVER_DB,NAME_DB

app=Flask(__name__)

#conctando base de datos con alchemy

USER_DB= USER_DB
USER_PASSWORD=USER_PASSWORD
SERVER_DB=SERVER_DB
NAME_DB=NAME_DB
FULL_URL_DB=f"mysql+pymysql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}"

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB

db=SQLAlchemy(app)

#migrar el modelo

migrate=Migrate()
migrate.init_app(app,db)

#modelo de datos

class Cursos(db.Model):
    id: Mapped[int]=mapped_column(primary_key=True)
    nombre:Mapped[str]=mapped_column(unique=True)
    instructor:Mapped[str]
    topico:Mapped[str]

    def __str__(self):
        return f"""
            id:{self.id}
            nombre:{self.nombre}
            instructor:{self.instructor}
            topico:{self.topico}
        """

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask,render_template
from db import db
from variables_entorno import NAME_BASE,NAME_USER,SERVER_NAME,SECRET_KEY,USER_PASSSWORD
from flask_migrate import Migrate
from models import Contacto
app=Flask(__name__)

FULL_URL_DB=f"mysql+pymysql://{NAME_USER}:{USER_PASSSWORD}@{SERVER_NAME}/{NAME_BASE}"


app.config["SQLALCHEMY_DATABASE_URI"]=FULL_URL_DB


db.init_app(app)
migrate=Migrate(app,db)


@app.route("/")
def inicio():
    contactos=Contacto.query.all()
    return render_template("index.html",contactos=contactos)

if __name__ == "__main__":
    app.run(debug=True)
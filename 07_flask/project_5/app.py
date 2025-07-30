from flask import Flask,render_template
from flask_migrate import Migrate
from db import db
from models import Frases
from variables_entorno import NAME_USER,SERVER_NAME,USER_PASSWORD,DATA_BASE,SECRET_KEY
import random

app=Flask(__name__)

FULL_URL_DB=f"mysql+pymysql://{NAME_USER}:{USER_PASSWORD}@{SERVER_NAME}/{DATA_BASE}"

app.config["SQLALCHEMY_DATABASE_URI"]=FULL_URL_DB

app.config["SECRET_KEY"]=SECRET_KEY

db.init_app(app)
migrate=Migrate(app,db)



@app.route("/")
def inicio():
    frases=Frases.query.all()
    frase=random.choice(frases)
    return render_template("index.html", data=frase)

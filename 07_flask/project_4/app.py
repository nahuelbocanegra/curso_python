from flask import Flask,render_template
from db import db
from flask_migrate import Migrate
from variables_entorno import NAME_BASE,NAME_USER,SERVER_NAME,SECRET_KEY,USER_PASSSWORD

app=Flask(__name__)

FULL_URL_DB=f"mysql+pymysql://{NAME_USER}:{USER_PASSSWORD}@{SERVER_NAME}/{NAME_BASE}"


app.config["SQLALCHEMY_DATABASE_URI"]=FULL_URL_DB


db.init_app(app)
migrate=Migrate(db,app)





@app.route("/")
def inicio():
    render_template("index.html")


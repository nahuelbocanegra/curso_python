from flask import Flask ,render_template 
from variables_entorno import DB_NAME,USER_NAME,SERVER_NAME,USER_PASSWORD,SECRET_KEY

app=Flask(__name__)

#conectando base de datos con alchemy
FULL_URL_DB=f"mysql+pymysql://{USER_NAME}:{USER_PASSWORD}@{SERVER_NAME}/{DB_NAME}"

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB



@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/mensaje/<int:id>")
def mensaje(id):
    pass
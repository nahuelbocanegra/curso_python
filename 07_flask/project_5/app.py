from flask import Flask,render_template
from flask_migrate import Migrate
from db import db
from models import Frases
from variables_entorno import NAME_USER,SERVER_NAME,USER_PASSWORD,DATA_BASE,SECRET_KEY

app=Flask(__name__)

FULL_URL_DB=f"mysql+pymysql://{NAME_USER}:{USER_PASSWORD}@{SERVER_NAME}/{DATA_BASE}"

app.config["SQLALCHEMY_DATABASE_URI"]=FULL_URL_DB

app.config["SECRET_KEY"]=SECRET_KEY

db.init_app(app)
migrate=Migrate(app,db)

@app.route("/")
def inicio():
    return render_template("index.html")

# "El éxito es la suma de pequeños esfuerzos repetidos día tras día."

# "No esperes el momento perfecto, toma el momento y hazlo perfecto."

# "El único lugar donde el éxito viene antes que el trabajo es en el diccionario."

# "Cree en ti y todo será posible."

# "Nunca es tarde para ser quien podrías haber sido."

# "Hazlo con pasión o no lo hagas."

# "El futuro pertenece a quienes creen en la belleza de sus sueños."

# "Si puedes soñarlo, puedes lograrlo."

# "Lo que no te mata, te hace más fuerte."

# "La vida comienza al final de tu zona de confort."

# "No vemos las cosas como son, las vemos como somos." – Anaïs Nin

# "La mente es todo. En lo que piensas, te conviertes." – Buda

# "No se puede descubrir nuevos océanos a menos que tengas el coraje de perder de vista la costa."

# "Aprender sin reflexionar es malgastar energía." – Confucio

# "El conocimiento habla, pero la sabiduría escucha." – Jimi Hendrix

# "Lo esencial es invisible a los ojos." – El Principito

# "Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un hábito." – Aristóteles

# "A veces perder es ganar."

# "No hay camino hacia la felicidad, la felicidad es el camino."

# "El tiempo que se disfruta es el verdadero tiempo vivido."
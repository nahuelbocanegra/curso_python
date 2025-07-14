from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class CursoForm(FlaskForm):
    nombre=StringField("Nombre",validators=[DataRequired()])
    Instructor=StringField("Instructor",validators=[DataRequired()])
    topico=StringField("Topico",validators=[DataRequired()])
    enviar=SubmitField("Enviar")

     
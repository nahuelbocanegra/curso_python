from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField,TextAreaField
from wtforms.validators import DataRequired 


class NuevoContacto(FlaskForm):
    nombre=StringField("Nombre",validators=[DataRequired])
    telefono=StringField("Telefono",validators=[DataRequired])
    email=StringField("Email",validators=[DataRequired])
    direccion=StringField("Direccion",)
    comentario=TextAreaField("comentario")
    enviar=SubmitField("Enviar")
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField , SubmitField #Importa un campo de texto (input tipo texto).
from wtforms.validators import DataRequired #Importa un validador que obliga a que el campo no esté vacío.

class MensajeForm(FlaskForm):
    titulo=StringField("Titulo del mensaje",validators=[DataRequired()])
    mensaje=TextAreaField("Mensaje",validators=[DataRequired()])
    enviar=SubmitField("Enviar")
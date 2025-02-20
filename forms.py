from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,  IntegerField, EmailField
from wtforms import validators


class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3,max=10,message="3-10 caracteres")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido=StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("Correo",[
        validators.Email(message="El campo es requerido")
    ])
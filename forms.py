from wtforms import Form
from wtforms import StringField, IntegerField, SelectField,EmailField, RadioField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido")
    ])

class ZodiacoForm(Form):
    nombre = StringField("Nombre", [validators.DataRequired("El nombre es requerido")])
    apellido_p = StringField("Apellido Paterno", [validators.DataRequired("El apellido paterno es requerido")])
    apellido_m = StringField("Apellido Materno", [validators.DataRequired("El apellido materno es requerido")])
    dia = IntegerField("Día", [validators.DataRequired("El día es requerido"), validators.NumberRange(min=1, max=31, message="Día inválido")])
    mes = IntegerField("Mes", [validators.DataRequired("El mes es requerido"), validators.NumberRange(min=1, max=12, message="Mes inválido")])
    anio = IntegerField("Año", [validators.DataRequired("El año es requerido"), validators.NumberRange(min=1900, max=2023, message="Año inválido")])
    sexo = RadioField("Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], validators=[validators.DataRequired("El sexo es requerido")])
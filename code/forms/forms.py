from flask_wtf import Form
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Email, Optional
from wtforms.fields.html5 import EmailField


class RegistrationForm(Form):
    name = StringField('Your full name', validators=[DataRequired()])
    email_address = EmailField('Your email address', validators=[DataRequired()])
    birthday = DateField('Your birthday', format='%d-%m-%Y', validators=[Optional()])

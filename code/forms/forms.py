from flask_wtf import Form
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Optional, ValidationError
from wtforms.fields.html5 import EmailField
from models import User


def validate_unique_name(form, field):
	if User.query.filter(User.name == field.data).first() is not None:
		raise ValidationError("User name already taken")


class RegistrationForm(Form):
    name = StringField('Your full name',
     validators=[DataRequired(), validate_unique_name])
    email_address = EmailField('Your email address',
     validators=[DataRequired()])
    birthday = DateField('Your birthday',
     format='%d-%m-%Y', validators=[Optional()])

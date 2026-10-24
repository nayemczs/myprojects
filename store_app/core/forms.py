from flask_security import RegisterForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])

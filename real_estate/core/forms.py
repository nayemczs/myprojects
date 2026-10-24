from flask_wtf import FlaskForm
from flask_security.forms import LoginForm
from wtforms.fields import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email


class ExtendedLoginForm(LoginForm):
    email = StringField('Email Address', validators=[DataRequired(message='EMAIL_NOT_PROVIDED'), Length(min=6)])
    password = PasswordField('Password', validators=[DataRequired(message='PASSWORD_NOT_PROVIDED'), Length(min=6)])


class FilterForm(FlaskForm):
    search = StringField()
    keyword = StringField()
    city = StringField()
    category = StringField()
    offer = StringField()
    bedrooms = StringField()
    bathrooms = StringField()
    space_range_min = StringField()
    space_range_max = StringField()
    order_by = StringField()


class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=6)])
    contact_no = StringField('Your Phone', validators=[DataRequired(), Length(min=6)])
    email = StringField('Your Email', validators=[DataRequired(), Email(), Length(min=6)])
    text = TextAreaField('Your Message', validators=[DataRequired(), Length(min=10)])


class AppointmentForm(FlaskForm):
    slot_id = HiddenField(DataRequired())
    name = StringField('Your Name', validators=[DataRequired(), Length(min=6)])
    contact_no = StringField('Your Phone', validators=[DataRequired(), Length(min=6)])
    email = StringField('Your Email', validators=[DataRequired(), Email(), Length(min=6)])

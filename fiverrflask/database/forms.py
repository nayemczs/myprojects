from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms.fields import HiddenField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    url = URLField(validators=[DataRequired(), URL()])


class DeleteAudioForm(FlaskForm):
    player_id = HiddenField(validators=[DataRequired()])

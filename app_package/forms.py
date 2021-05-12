from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class DarkToggleForm(FlaskForm):
    is_dark = BooleanField('Dark Theme')


class TagManagerForm(FlaskForm):
    tag_input = SelectMultipleField('Interest tags')
    submit = SubmitField('Update')


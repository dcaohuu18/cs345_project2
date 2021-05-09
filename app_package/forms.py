from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class TagManagerForm(FlaskForm):
    tag_input = SelectMultipleField('Interest tags')
    submit = SubmitField('Update')


from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

avail_tags = [
('world news', 'world news'), 
('sports', 'sports'),
('covid', 'covid')
] # (value, label)

class TagManagerForm(FlaskForm):
    tag_manager = SelectMultipleField('Interest tags', validators=[DataRequired()], 
                                      choices=avail_tags)
    submit = SubmitField('Update')

    
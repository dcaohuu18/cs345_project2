from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    #usernames are required, and they must be between 2 and 20 chars long
    username = StringField("Username", validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

#We probably don't need this since there's only one user
class LogInForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log In")

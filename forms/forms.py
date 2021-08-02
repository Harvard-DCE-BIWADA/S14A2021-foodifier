from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Signup')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UpdateGoals(FlaskForm):
    dgoal = IntegerField('Daily Calorie Goal', validators = [DataRequired()]) 
    wgoal = IntegerField('Weekly Calorie Goal', validators = [DataRequired()]) 
    submit = SubmitField('Update Goals')

class UpdateAccount(FlaskForm):
    username = StringField('Username', validators = [DataRequired()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Account')

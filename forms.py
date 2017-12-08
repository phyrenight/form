from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class WebForm(FlaskForm):
    email = StringField(
        'email',
        validators=[DataRequired('Please enter your email address')])
    question_one = SelectField(
        'Coke or Pepsi',
        choices=[('None', 'None'), ('Pepsi', 'Pepsi'), ('Coke', 'Coke')],
        validators=[DataRequired('Please answer this question')])
    submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class WebForm(FlaskForm):
    first_name = StringField(
        'First name',
        validators=[DataRequired('Please enter your first name')])
    last_name = StringField(
        'Last name',
        validators=[DataRequired('Please enter your last name')])
    address = StringField(
        'address',
        validators=[])
    email = StringField(
        'email',
        validators=[DataRequired('Please enter your email address')])
    phone_number = StringField(
        'Phone number',
        validators=[DataRequired('Please enter your phone number')])
    question_one = SelectField(
        'Coke or Pepsi',
        choices=[('None', 'None'), ('Pepsi', 'Pepsi'), ('Coke', 'Coke')],
        validators=[DataRequired('Please answer this question'),
        Email('Please enter a valid email address')])
    submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
        'phone number',
        validators=[DataRequired('Please enter your phone number')])
    question_one = StringField(
        'quetion one',
        validators=[DataRequired('Please answer this question'),
        Email('Please enter a valid email address')])
    submit = Submit('Submit')
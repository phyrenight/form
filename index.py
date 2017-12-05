from flask import Flask, render_template
from questionaire_db import Answer

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    form = Answer()
    return render_template('home.html', form=form)

@app.route('/')
def summary():
    return render_template('summary')

from flask import Flask, render_template
from config import secret_key
from questionaire_db import Answers, session as db_session
from forms import WebForm

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/')
@app.route('/home')
def home():
    form = WebForm()
    return render_template('home.html', form=form)

@app.route('/')
def summary():
    # db_session.query
    return render_template('summary')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, request, url_for
from config import secret_key
from questionaire_db import Answers, session as db_session
from forms import WebForm

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = WebForm()
    if request.method == 'POST':
    	return redirect(url_for('results'))

    return render_template('home.html', form=form)

@app.route('/results')
def results():
    pepsi_count = db_session.query(Answers).filter(Answers.question_one == 'Pepsi').count()
    coke_count = db_session.query(Answers).filter(Answers.question_one == 'Coke').count()
    print coke_count
    print pepsi_count
    return render_template(
    	'results.html',
        coke_count=coke_count,
        pepsi_count=pepsi_count)

if __name__ == "__main__":
    app.run(debug=True)
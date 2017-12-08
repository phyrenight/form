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
        if form.validate() is False:
            return render_template('home.html', form=form)
        else:
            question_one = form.question_one.data
            print question_one
            answer = Answers(
                form.email.data,
                question_one)
            db_session.add(answer)
            db_session.commit()
    	    return redirect(url_for('results'))
    else:
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
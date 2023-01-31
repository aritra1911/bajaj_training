from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

class TestForm(FlaskForm):
    cat_breed = StringField('What is the cat breed?')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    cat_breed: str = ''
    form: FlaskForm = TestForm()

    if form.validate_on_submit():
        cat_breed = form.cat_breed.data
        form.cat_breed.data = ''

    return render_template('forms.html', cat_breed=cat_breed, form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (
    StringField, BooleanField, DateTimeField, RadioField, SelectField,
    TextAreaField, SubmitField
)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyS3Re7K3Y'

class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me!')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash('You just clicked the button!')
        return redirect(url_for('index'))
    return render_template('home3.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
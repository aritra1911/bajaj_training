from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
    StringField, BooleanField, DateTimeField, RadioField, SelectField,
    TextAreaField, SubmitField
)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys3cr3tk3y'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    tomcat = BooleanField('Have you been tomcat?')
    mood = RadioField('Please Choose your mood:', choices=[
        ('mood_one', 'happy'),
        ('mood_one', 'excited')
    ])
    food_choice = SelectField('Pick your favorite food:', choices=[
        ('chi', 'Chicken'),
        ('bef', 'Beef'),
        ('fish', 'Fish')
    ])
    when_is_this = StringField()
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    session.clear()
    if form.validate_on_submit():
        for field in form:
            session[field.name] = field.data
        #return redirect(url_for('thankyou'))
    return render_template('home1.html', form=form, session=session)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=6666)
    app.run(debug=True)
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email

class StudentForm(FlaskForm):
    name = StringField('სახელი', validators=[DataRequired()])
    email = StringField('მეილი', validators=[DataRequired(), Email()])
    course = StringField('კურსი', validators=[DataRequired()])
    grade = FloatField('შეფასება', validators=[DataRequired()])
    submit = SubmitField('დამატება')

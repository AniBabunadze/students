from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import StudentForm
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'students.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_123'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    course = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Student {self.name}>"

# პირველი გაშვებისას ერთი ჩაირთე ტერმინალში რომ შეიქმნას ბაზა:
# >>> from app import db, app
# >>> with app.app_context():
# >>>     db.create_all()


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Student(
            name=form.name.data,
            email=form.email.data,
            course=form.course.data,
            grade=form.grade.data
        )
        db.session.add(new_student)
        db.session.commit()
        flash("სტუდენტი წარმატებით დაემატა!", "success")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

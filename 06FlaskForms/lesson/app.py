from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column(db.String(120), nullable=False)


class LoginForm(FlaskForm):
    username: str = StringField('Username', validators=[DataRequired()])
    password: str = PasswordField('Password', validators=[DataRequired()])
    submit: str = SubmitField('Submit')


@app.route('/')
def login():
    form: LoginForm = LoginForm()
    return render_template('index.html', form=form)


@app.route('/submit', methods=['POST'])
def submit_form():
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        username: str = form.username.data
        password: str = form.password.data
        new_user: User = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'User added to database!'
    return render_template('login.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
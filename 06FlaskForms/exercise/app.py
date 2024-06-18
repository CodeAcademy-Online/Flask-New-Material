from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    password: str = db.Column(db.String(120), nullable=False)


class LoginForm(FlaskForm):
    email: str = StringField('Email', validators=[DataRequired(), Email()])
    password: str = PasswordField('Password', validators=[DataRequired()])
    submit: str = SubmitField('Login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email: str = request.form['email']
        password: str = request.form['password']
        new_user: User = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'Successful registration!'
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        email: str = form.email.data
        password: str = form.password.data
        user: User = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return 'Logged in successfully!'
        return 'Incorrect email or password.'
    return render_template('login.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

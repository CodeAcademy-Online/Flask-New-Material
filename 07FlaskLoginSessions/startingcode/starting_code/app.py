from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key'  # Change this to a secure secret key


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'

@app.route('/logout')
def logout():
    return 'logout'

if __name__ == '__main__':
    app.run(debug=True)

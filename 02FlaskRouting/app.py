from flask import Flask
from flask import Response

app: Flask = Flask(__name__)

@app.route('/')
def first_page() -> Response:
    return 'My first page'

@app.route('/profile/<name>')
def profile(name) -> Response:
    return f'Profile page of... {name}'

if __name__ == '__main__':
    app.run(debug=True)
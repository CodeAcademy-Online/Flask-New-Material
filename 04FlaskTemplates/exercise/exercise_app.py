from flask import Flask, render_template, Response

app: Flask = Flask(__name__)

posts = [
    {
        'date': '2011-11-11',
        'author': 'Author1',
        'title': 'Title1',
        'content': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum'
    },
    {
        'date': '2012-10-11',
        'author': 'Author2',
        'title': 'Title2',
        'content': 'test test test test test test test test test test test test test test'
    },
    {
        'date': '2022-05-25',
        'author': 'Author3',
        'title': 'Title3',
        'content': 'content content content content content content content content content content'
    }
]

@app.route('/')
def index() -> Response:
    name = "John"
    return render_template('index.html', name=name, posts=posts) #exercise 1, exercise 2

@app.route('/')
def profile() -> Response:
    return render_template('profile.html')



if __name__ == '__main__':
    app.run(debug=True)
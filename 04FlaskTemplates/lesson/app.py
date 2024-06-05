from flask import Flask, render_template, Response

app: Flask = Flask(__name__)

posts = [
    {
        'date': '2011-11-11',
        'author': 'Author1',
        'title': 'Sveiki, cia mano blogas pirmas postas',
        'content': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum'
    },
    {
        'date': '2012-10-11',
        'author': 'Author2',
        'title': 'Title2',
        'content': 'Hahaha as ismokau Python'
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
    return render_template("index.html", name="Panda", posts=posts)

@app.route('/profile/<username>')
def profile(username) -> Response:
    return render_template("profile.html", name=username)


if __name__ == '__main__':
    app.run(debug=True)
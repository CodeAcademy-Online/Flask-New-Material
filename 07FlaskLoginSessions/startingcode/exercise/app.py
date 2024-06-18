from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret129381IIMDQSMD831Key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    if "username" in session:
        user = User.query.filter_by(username=session["username"]).first()
        user_posts = Post.query.filter_by(user_id=user.id).all()
        return render_template("index.html", username=session["username"], posts=user_posts)
    else:
        return render_template("index.html", posts=[])


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = "Jonas"
        password = "jonas12312"
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template("register.html", message="User with such username already exists!")
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("register.html", message="Registered successfully. You can log in now!", registered=True)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return redirect(url_for("home"))
        else:
            return render_template("login.html", message="Invalid username or password!")
    return render_template("login.html")


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        user = User.query.filter_by(username=session["username"]).first()
        new_post = Post(title=title, content=content, user_id=user.id)
        return redirect(url_for("home"))
    return render_template("create_post.html")


@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if "username" not in session:
        return redirect(url_for("login"))
    post = Post.query.get(post_id)
    user = User.query.get(post.user_id)
    if user.username != session["username"]:
        return redirect(url_for("home"))
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_post.html", post=post)


@app.route("/view_post/<int:post_id>")
def view_post(post_id):
    post = Post.query.get(post_id)
    user = User.query.get(post.user_id)
    if post:
        return render_template("view_post.html", post=post)
    else:
        return redirect(url_for("home"))


@app.route("/delete_post/<int:post_id>")
def delete_post(post_id):
    if "username" not in session:
        return redirect(url_for("login"))
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

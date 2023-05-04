import hashlib
from app import app, db
from flask import render_template, request, redirect, session, abort
from models import User, Articles


@app.route("/")
def articles():
    articles = Articles.query.all()
    return render_template("index.html", articles=articles)

@app.route("/article/<int:article_id>/edit", methods=["GET", "POST"])
def article_edit(article_id):
    if session.get("user"):
        article = Articles.query.get_or_404(article_id)

        if article.user_id != session["user"]["id"]:
            abort(403)

        if request.method == "GET":
            return render_template("article-edit.html", article=article)

        if request.method == "POST":
            article.title = request.form["title"]
            article.body = request.form["body"]

            db.session.commit()

        return redirect("/")

    else:
        return render_template("sign-in.html")


@app.route("/article/<int:article_id>/delete", methods=["POST"])
def article_delete(article_id):
    if session.get("user"):
        article = Articles.query.get_or_404(article_id)

        if article.user_id != session["user"]["id"]:
            abort(403)

        if request.method == "POST":
            db.session.delete(article)
            db.session.commit()

        return redirect("/")

    else:
        return render_template("sign-in.html")

@app.route("/article/create")
def article_create():
    if session.get("user"):
        return render_template('article-create.html')
    else:
        return render_template("sign-in.html")


@app.route("/save-article", methods=["POST"])
def save_article():
    data = request.form
    article = Articles(title=data.get('title'), body=data.get("body"), user_id=session.get('user').get("id"))
    db.session.add(article)
    db.session.commit()
    return redirect("/")


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/save-user", methods=["POST"])
def register():
    data = request.form
    password_hash = hashlib.sha256(data.get("password").encode("utf-8"))
    user = User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        password=password_hash.hexdigest(),
    )
    db.session.add(user)
    db.session.commit()
    session["user"] = user.serialize
    return redirect("/")


@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")


@app.route("/authorize", methods=["POST"])
def authorize():
    data = request.form
    user = User.query.filter(User.email == data.get("email")).first()
    if user:
        if hashlib.sha256(data.get("password").encode("utf-8")).hexdigest() == user.password:
            session["user"] = user.serialize
    return redirect("/")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")

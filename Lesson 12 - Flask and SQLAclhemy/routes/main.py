import hashlib

from flask import request, session, redirect, render_template, flash
from app import app, db
from models import User


@app.route("/")
def index():
    # this code represent read
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def create():
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
    return redirect("/")

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)

    data = request.form
    password_hash = hashlib.sha256(data.get("password").encode("utf-8"))
    user.first_name = data.get("first_name")
    user.last_name = data.get("last_name")
    user.email = data.get("email")
    user.password = password_hash.hexdigest()

    db.session.commit()

    return redirect("/")

@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/")

from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
# from models import *

import os
app = Flask(__name__)

@app.route("/")
def index():
    # boom = os.path.join('moerbijboom.jpg')
    return render_template("index.html")

@app.route("/info", methods=['POST', 'GET'])
def info():
    if request.method == 'GET':
        return render_template("info.html")


    elif request.method == "POST":
        return render_template("track.html")



@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    # session.clear()

    if request.method == "GET":
        return render_template("register.html")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # request username, password, confirmation
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not request.form.get("username"):
            errortext = "Username was not submitted"
            return render_template("error.html", errortext=errortext)

        # Ensure password was submitted
        elif not request.form.get("password"):
            errortext = "Password was not submitted"
            return render_template("error.html", errortext=errortext)

        elif not request.form.get("confirmation"):
            errortext = "confirmation was not submitted"
            return render_template("error.html", errortext=errortext)

        elif password != confirmation:
            errortext = "passwords differ"
            return render_template("error.html", errortext=errortext)

        # Create a hash of the password
        hash = generate_password_hash(password)

        # Add this to the database:
        user = Users(username=username, password=hash)
        db.session.add(user)
        db.session.commit()


        # Remember which user has logged in
        session[username] = username

        # Redirect user to home page
        return redirect("/")


@app.route('/game_rules', methods=['POST', 'GET'])
def game_rules():
    if request.method == "GET":
        return render_template("game_rules.html")

    elif request.method == "POST":
        return render_template("game_rules.html")

@app.route('/history', methods=['POST', 'GET'])
def history():
    if request.method == "GET":
        return render_template("history.html")

    elif request.method == "POST":
        return render_template("history.html")

@app.route('/friends', methods=['POST', 'GET'])
def friends():
    if request.method == "GET":
        return render_template("friends.html")

    elif request.method == "POST":
        return render_template("friends.html")

@app.route('/friend_request', methods=['POST', 'GET'])
def friend_request():
    if request.method == "GET":
        return render_template("friend_request.html")

    elif request.method == "POST":
        return render_template("friend_request.html")

@app.route('/poll', methods=['POST', 'GET'])
def poll():
    if request.method == "GET":
        return render_template("poll.html")

    elif request.method == "POST":
        return render_template("poll.html")

@app.route('/track', methods=['POST', 'GET'])
def track():
    if request.method == "GET":
        return render_template("track.html")

    elif request.method == "POST":
        return render_template("track.html")

from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route("/")
def index():
    # boom = os.path.join('moerbijboom.jpg')
    return render_template("index.html")

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

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

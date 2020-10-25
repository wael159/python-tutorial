# __init__.py
import flask
from flask import render_template
app = flask.Flask(__name__) # __name__ is the name of the folder
#rom models.py import users
#from . import models.py
@app.route("/")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="My awesome app", title2="Awesome app")


@app.route("/profile/<user_name>")
def profile_page(user_name):
    if user_name=='wael':
        return flask.render_template("index.html", title="My awesome app", title2="Awesome app")
    else:
        return "User not found"

    #return flask.render_template("profile_page.html", user=user)


app.run()
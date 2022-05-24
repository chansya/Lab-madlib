"""A madlib game that compliments its users."""

from random import choice
import re

from flask import Flask, redirect, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user, ask if they want to play"""

    player = request.args.get("person")

    return render_template("madlib_game.html", person=player)


@app.route("/game")
def show_madlib_form():
    """Get user's reponse of if they want to play game, if yes then play, if no goodbye"""

    play = request.args.get("play")

    if play == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route("/madlib", methods=["GET","POST"])
def show_madlib():
    if request.method=="GET":
        return redirect("/hello")

    person = request.form.get("person")
    noun = request.form.get("noun")
    color = request.form.get("color")
    adj_list = request.form.getlist("adj")
    # need .getlist to use multiple checkboxes 
    
    return render_template("madlib.html", person=person, noun=noun, color=color, adjs=adj_list)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

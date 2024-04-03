# Flask is a web framework for Python. It is used to create web applications.
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Create a Flask app
app.secret_key = "comples" # Secret key for session
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3" # Database URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Disable modification tracking
app.permanent_session_lifetime = timedelta(minutes=30) # Set the session lifetime to 30 minutes

db = SQLAlchemy(app) # Create a database

class users(db.Model): # Create a database model
    _id = db.Column("id", db.Integer, primary_key=True) # ID column
    name = db.Column(db.String(100)) # Name column
    email = db.Column(db.String(100)) # Email column

    def __init__(self, name, email): # Constructor method, takes in name and email
        self.name = name
        self.email = email


@app.route("/") 
def home(): # Home page 
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login(): # Login page
    if request.method == "POST":
        session.permanent = True # Set the session to permanent
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user")) # Redirect to the user page
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user(): # User page
    email = None
    if "user" in session:
        user = session["user"] # Get the user from the session

        # this is not working 
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", user=user)
    else:
        flash ("You are not logged in!", "info")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout(): # Logout page
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out! {user}", "info") # Flash message , info is the category there aro 4 types of categories: primary, secondary, success, danger
    session.pop("user", None) # Remove the user from the session
    session.pop("email", None)
    return redirect(url_for("login")) # Redirect to the login page

if __name__ == "__main__":
    db.create_all() # Create the database
    app.run(debug=True) # Run the Flask app, debug=True will print out possible Python errors on the web page
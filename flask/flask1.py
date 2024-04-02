# Flask is a web framework for Python. It is used to create web applications.
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__) # Create a Flask app
app.secret_key = "comples" # Secret key for session
app.permanent_session_lifetime = timedelta(minutes=30) # Set the session lifetime to 30 minutes

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

@app.route("/user")
def user(): # User page
    if "user" in session:
        user = session["user"] # Get the user from the session
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
    return redirect(url_for("login")) # Redirect to the login page

if __name__ == "__main__":
    app.run(debug=True) # Run the Flask app, debug=True will print out possible Python errors on the web page
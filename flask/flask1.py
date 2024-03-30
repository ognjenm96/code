# Flask is a web framework for Python. It is used to create web applications.
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # Create a Flask app

@app.route("/<name>") # Home page 
def home(name):
    # render_template() function is used to render a template.
    return render_template("index.html")







@app.route("/<name>") # app.route() decorator to tell Flask what URL should trigger the function
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    # redirect() function is used to redirect the user to another endpoint or URL.
    return redirect(url_for("user", name="Admin")) # Redirect to the user() function

if __name__ == "__main__":
    app.run()
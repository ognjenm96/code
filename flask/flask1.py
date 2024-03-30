# Flask is a web framework for Python. It is used to create web applications.
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # Create a Flask app

@app.route("/<name>") # Home page 
def home(name):
    return render_template("index.html", content = name, r=2)

if __name__ == "__main__":
    app.run()
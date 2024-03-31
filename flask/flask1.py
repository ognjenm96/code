# Flask is a web framework for Python. It is used to create web applications.
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # Create a Flask app

@app.route("/") # Home page 
def home():
    # render_template() function is used to render a template.
    # It takes the name of the HTML file as an argument.
    # The HTML file should be in a templates folder in the same directory as the script.
    # The content variable is passed to the HTML file.
    # The content variable is used to display the name on the web page.
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("")

@app.route("/user/<usr>")
def user(usr):
    return render_template("")

if __name__ == "__main__":
    app.run(debug=True) # Run the Flask app, debug=True will print out possible Python errors on the web page
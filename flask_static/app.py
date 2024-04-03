from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_static.admin.admin_app import admin_app
import os

app = Flask(__name__) # Create a Flask app
app.register_blueprint(admin_app, url_prefix="/admin") # Register the blueprint

@app.route("/")
def test():
    return "<h1>Test</h1>" # Render the template

if __name__ == "__main__":
    app.run(debug=True) # Run the app in debug mode
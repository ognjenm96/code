from flask import Blueprint, render_template

admin_app = Blueprint("admin_app", __name__, static_folder="static", template_folder="templates")

@admin_app.route("/home")
@admin_app.route("/")
def home():
    return render_template("home.html")
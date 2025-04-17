from flask import render_template, request, redirect, url_for, session
from database import validate_login, get_suggestions, get_user_preferences
from messaging import prepare_message

def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            distributor = request.form["distributor"]
            if validate_login(distributor):
                session["distributor"] = distributor
                return redirect(url_for("home"))
            else:
                return render_template("login.html", error="Accès refusé.")
        return render_template("login.html")

    @app.route("/home", methods=["GET", "POST"])
    def home():
        if "distributor" not in session:
            return redirect(url_for("login"))
        distributor = session["distributor"]
        preferences = get_user_preferences(distributor)
        suggestions = get_suggestions(distributor, preferences)
        return render_template("home.html", suggestions=suggestions)

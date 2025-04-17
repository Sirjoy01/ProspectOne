from flask import render_template
from run import app

@app.route("/")
def index():
    return "Index fonctionne bien !"

@app.route("/test")
def test():
    return "Test fonctionne bien !"

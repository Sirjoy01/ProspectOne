from flask import Flask
from app.routes import *
from utils.database import init_db

app = Flask(_ _name_ _)

if _ _name_ _ == "_ _main_ _":
    init_db()
    app.run(host="0.0.0.0", port=5000)


app = app

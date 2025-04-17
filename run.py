from flask import Flask
from routes import *
from database import init_db

app = flask_app
flask_app = Flask(__name__)

if __name__ == "__main__":
    init_db()
    flask_app.run(host="0.0.0.0", port=5000)



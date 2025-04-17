from flask import Flask
from routes import *
from database import init_db

flask_app = Flask(__name__)
app = flask_app

if __name__ == "__main__":
    init_db()
    flask_app.run(host="0.0.0.0", port=5000)



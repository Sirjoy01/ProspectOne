from flask import Flask
from routes import *
from utils.database import init_db

app = Flask(__name__)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)

app = app

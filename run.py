from flask import Flask
from routes import *
from database import init_db

app = Flask(__name__)
app.secret_key = "ma_clé_secrète"
init_db()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

app = app

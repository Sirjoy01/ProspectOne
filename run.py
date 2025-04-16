from app import app
from app.routes import *
from utils.database import init_db

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0")
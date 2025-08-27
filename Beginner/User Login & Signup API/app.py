from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from routes import *  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

from flask import Flask, request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
app.config['SQL_ALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    with app.app.context():
        db.create_all()
    app.run(debug = True)

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
# from models import User

app = Flask(__name__)
auth = HTTPBasicAuth()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from routes import *

# with app.app_context():
#     db.create_all()
#     if not User.query.filter_by(username="admin").first():
#         hashed_pw = generate_password_hash("secret")
#         db.session.add(User(username="admin", password=hashed_pw))
#         db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config import Config
import stripe
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)
stripe.api_key = app.config["STRIPE_API_KEY"]

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(70), nullable = False, unique = True)
    password = db.Column(db.String(20), nullable = False)
    role = db.Column(db.String(20), default = "client")
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'))
    

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    plan = db.Column(db.String(10))
    price = db.Column(db.Float)
    users = db.relationship('User', backref='subscription')
    

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    users = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    status = db.Column(db.String(15), default= 'pending')
    created_at = db.Column(db.DateTime, default = datetime.utcnow)


@app.before_first_request
def create_tables():
    db.create_all()
    if not Subscription.query.first():
        db.session.add_all([
            Subscription(plan="Free", price=0),
            Subscription(plan="Pro", price=10),
            Subscription(plan="Premium", price=30)
        ])
        db.session.commit()
        
from routes import *

if __name__ == "__main__":
    app.run(debug = True)
import os

class Config:
    SECRET_KEY = "your-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///saas.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "your-jwt-secret"
    STRIPE_API_KEY = "sk_test_yourkey"

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default="client")  # client, admin
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(50))  # Free, Pro, Premium
    price = db.Column(db.Float)
    users = db.relationship("User", backref="subscription")

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    amount = db.Column(db.Float)
    status = db.Column(db.String(20), default="pending")  # pending, paid
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User, Subscription, Invoice
from config import Config
import stripe

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)
stripe.api_key = app.config["STRIPE_API_KEY"]

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

# --- Auth Routes ---
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(username=data["username"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(msg="User registered")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"], password=data["password"]).first()
    if not user:
        return jsonify(msg="Bad credentials"), 401
    token = create_access_token(identity=user.id)
    return jsonify(access_token=token)

# --- Subscription Routes ---
@app.route("/subscribe", methods=["POST"])
@jwt_required()
def subscribe():
    user_id = get_jwt_identity()
    data = request.json
    subscription = Subscription.query.filter_by(plan=data["plan"]).first()
    if not subscription:
        return jsonify(msg="Plan not found"), 404
    
    user = User.query.get(user_id)
    user.subscription = subscription
    invoice = Invoice(user_id=user.id, amount=subscription.price, status="pending")
    
    db.session.add(invoice)
    db.session.commit()
    return jsonify(msg=f"Subscribed to {subscription.plan}", invoice_id=invoice.id)

# --- Billing Routes ---
@app.route("/pay/<int:invoice_id>", methods=["POST"])
@jwt_required()
def pay(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify(msg="Invoice not found"), 404
    
    # Simulation Stripe PaymentIntent
    payment_intent = stripe.PaymentIntent.create(
        amount=int(invoice.amount * 100),  # cents
        currency="usd",
        payment_method_types=["card"],
    )
    invoice.status = "paid"
    db.session.commit()
    return jsonify(msg="Payment successful", client_secret=payment_intent.client_secret)

# --- Admin View ---
@app.route("/admin/invoices", methods=["GET"])
@jwt_required()
def all_invoices():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user.role != "admin":
        return jsonify(msg="Unauthorized"), 403
    
    invoices = Invoice.query.all()
    return jsonify([{"id": i.id, "amount": i.amount, "status": i.status} for i in invoices])

if __name__ == "__main__":
    app.run(debug=True)

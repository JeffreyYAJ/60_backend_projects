from flask import Flask, request, jsonify
from app import app, db, User, Subscription, Invoice

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import stripe



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

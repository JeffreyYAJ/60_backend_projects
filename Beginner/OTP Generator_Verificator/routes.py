from flask import Flask, request, jsonify
from app import app
import pyotp
import time

otp_store = {}

@app.route("/generate_password", methods=["POST"])
def generate_otp():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username required"}), 400

    username = data["username"]

    
    secret = pyotp.random_base32()

    # OTP TOTP valide 60 secondes
    totp = pyotp.TOTP(secret, interval=60)
    otp_code = totp.now()

    # Stocker l’OTP et sa clé secrète
    otp_store[username] = {
        "secret": secret,
        "created_at": time.time()
    }

    return jsonify({
        "message": "OTP generated",
        "username": username,
        "otp": otp_code,
        "expires_in": 60
    }), 200


@app.route("/validate-otp", methods=["POST"])
def validate_otp():
    data = request.get_json()

    if not data or "username" not in data or "otp" not in data:
        return jsonify({"error": "Username and OTP required"}), 400

    username = data["username"]
    otp_code = data["otp"]


    if username not in otp_store:
        return jsonify({"error": "No OTP generated for this user"}), 404

    record = otp_store[username]
    totp = pyotp.TOTP(record["secret"], interval=60)

    if totp.verify(otp_code):
        del otp_store[username]  
        return jsonify({"message": "OTP is valid"}), 200
    else:
        return jsonify({"error": "Invalid or expired OTP"}), 400
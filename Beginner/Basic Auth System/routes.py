from app import db, auth, app
from flask import jsonify, request
from werkzeug.security import check_password_hash,generate_password_hash
from models import User

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

@app.route('/')
@auth.login_required
def index():
    return jsonify({"message": f"Hello, {auth.current_user().username}!"})

@app.route('/add_user', methods=['POST'])
@auth.login_required
def add_user():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing username or password"}), 400
    
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "User already exists"}), 400
    
    hashed_pw = generate_password_hash(data["password"])
    new_user = User(username=data["username"], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": f"User {data['username']} created successfully"}), 201

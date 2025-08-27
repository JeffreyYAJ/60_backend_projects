from flask import Flask, request, jsonify
from models import User
from app import db, app

@app.route("/user/signup", methods = ['POST'])
def user_signup():
    data = request.get_json()
    new_user = User( user_name = data['username'], email = data['email'], password = data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"Message":"Utilisateur creer"})

@app.route("/users/get_all", methods = ["GET"])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({"id": user.id, "username": user.user_name, "email": user.email})
    return jsonify(users_list)
    
@app.route("/user/login", methods = ['POST'])
def user_login():
    data = request.get_json()
    
    try:
        logged_username = User.query.filter_by(user_name= data['username'], password=data['password']).first()
        logged_email = User.query.filter_by(email = data['email'], password = data['password']). first()
    
    except(KeyError):
        pass
    
    if logged_username or logged_email:
        return jsonify({"Message": "Connexion etablie"})
    return jsonify({"Message": "Identifiant erronne"})
     
    
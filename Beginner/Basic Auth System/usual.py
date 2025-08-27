from models import User
from app import db, auth
from werkzeug.security import check_password_hash, generate_password_hash


@auth.verify_password
def verify_pass(username, password):
    user = User.query.filter_by(username= username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
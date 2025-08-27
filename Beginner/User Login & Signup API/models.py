from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(70), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    
    def __init__(self, user_name, email, password ):
        self.user_name = user_name
        self.email = email
        self.password = password
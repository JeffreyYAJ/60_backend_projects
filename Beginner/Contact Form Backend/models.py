from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    number = db.Column(db.String(15), nullable = False)
    email = db.Column(db.String(70), nullable = True)
    
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
        
    
from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(200), nullable = False, unique = True)
    shorten_url = db.Column(db.String(100), nullable = False, unique = True)
    created_at = db.Column(db.DateTime, nullable = False)
    
    def __init__(self, original_url, shorten_url, created_at):
        self.original_url = original_url
        self.shorten_url = shorten_url
        self.created_at = created_at
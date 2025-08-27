from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    content = db.Column(db.String(500), nullable = False)
    author = db.Column(db.Text, nullable =False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    
    
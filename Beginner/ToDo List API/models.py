from flask_sqlalchemy import SQLAlchemy
from app import db

class Tache(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    titre = db.Column(db.String(500), nullable= False)
    description = db.Column(db.String(1000), nullable=True)
    creation_date = db.Column(db.DateTime, nullable = False)
    end_date =  db.Column(db.DateTime, nullable =False)
    
    def __init__(self, titre, description, creation_date, end_date):
        self.titre = titre
        self.description = description
        self.creation_date = creation_date
        self.end_date = end_date
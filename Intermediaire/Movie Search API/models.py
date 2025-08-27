from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primar_key  =True)
    name = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(200), nullable = True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'year': self.year,
            'description': self.description
        }
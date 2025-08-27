from app import db

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.relationship('Option', backref='poll', lazy=True)

    def __init__(self, question):
        self.question = question
        self.options = []
    
class Option(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable = False)
    option_text = db.Column(db.String(200), nullable = False)
    votes = db.Column(db.Integer, default=0)
    poll = db.relationship('Poll', back_populates = 'options')
    
    def __init__(self, option_text):
        self.option_text = option_text
        self.votes = 0
        self.poll = None
        self.poll_id = None
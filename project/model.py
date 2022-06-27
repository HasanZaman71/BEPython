from project import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    complete = db.Column(db.Boolean, nullable=True)

    def __init__(self, title, complete):
        self.title = title
        self.complete = complete 

from main import db
from time import time

class User(db.Model):
    __tablename__ = 'miniurl_users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(320), unique=True, nullable=False)
    created_at = db.Column(db.String(10), default=int(time()))

    links = db.relationship('Link', backref='users')

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at
        }
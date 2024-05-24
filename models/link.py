from main import db
from time import time

class Link(db.Model):
    __tablename__ = 'miniurl_links'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('miniurl_users.id'), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    hash = db.Column(db.String(22), unique=True, nullable=False)
    long_url = db.Column(db.String(2048), nullable=False)
    created_at = db.Column(db.String(10), default=int(time()))
    clicks = db.Column(db.Integer, default=0)

    stats = db.relationship('Stat', backref='links')

    def serialize(self):
        return {
            'id': self.id,
            'uid': self.uid,
            'title': self.title,
            'hash': self.hash,
            'long_url': self.long_url,
            'created_at': self.created_at,
            'clicks': self.clicks
        }
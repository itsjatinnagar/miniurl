from main import db
from time import time

class Stat(db.Model):
    __tablename__ = 'miniurl_stats'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lid = db.Column(db.Integer, db.ForeignKey('miniurl_links.id'), nullable=False)
    user_agent = db.Column(db.Text, nullable=False)
    redirect_at = db.Column(db.String(10), default=int(time()))

    def serialize(self):
        return {
            'id': self.id,
            'lid': self.lid,
            'user_agent': self.user_agent,
            'redirect_at': self.redirect_at
        }
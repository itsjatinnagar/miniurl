from models.stat import Stat
from main import db

class StatController:
    @staticmethod
    def get_stat(lid):
        return Stat.query.filter_by(lid=lid).all()
    
    @staticmethod
    def create_stat(data):
        stat = Stat(lid = data['lid'], user_agent = data['user_agent'])
        db.session.add(stat)
        db.session.commit()
        return stat
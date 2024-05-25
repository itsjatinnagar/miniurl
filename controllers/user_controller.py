from models.user import User
from main import db

class UserController:
    @staticmethod
    def create_user(data):
        user = User.query.filter_by(email = data['email']).first()
        if user:
            return user
        user = User(email = data['email'])
        db.session.add(user)
        db.session.commit()
        return user
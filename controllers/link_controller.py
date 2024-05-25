from models.link import Link
from main import db

class LinkController:
    @staticmethod
    def get_link(hash):
        return Link.query.filter_by(hash = hash).first()
    
    @staticmethod
    def get_links(uid):
        return Link.query.filter_by(uid=uid).all()

    @staticmethod
    def create_link(data):
        link = Link(uid= data['uid'], title= data['title'], hash= data['hash'], long_url= data['long_url'])
        db.session.add(link)
        db.session.commit()
        return link
    
    @staticmethod
    def update_link(id, data):
        link = Link.query.get(id)
        if link:
            link.title = data.get('title', link.title)
            link.hash = data.get('hash', link.hash)
            link.clicks = data.get('clicks', link.clicks)
            db.session.commit()
            return link
        return None

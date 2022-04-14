from datetime import datetime
from api.models.db import db

class Personality(db.Model):
    __tablename__ = 'personalities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    birthYear = db.Column(db.Integer)
    ans_1 = db.Column(db.String(100))
    ans_2 = db.Column(db.String(100))
    ans_3 = db.Column(db.String(100))
    ans_4 = db.Column(db.String(100))
    ans_5 = db.Column(db.String(100))
    comment = db.Column(db.String(250))
    zodiac = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
      return f"Personality('{self.id}', '{self.name}')"

    def serialize(self):
      personality = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return personality
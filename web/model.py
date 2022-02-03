from sqlalchemy.sql import func
from . import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(10000),nullable=False)
    short_url = db.Column(db.String(100),nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

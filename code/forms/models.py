from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime)
    registered_at = db.Column(db.DateTime, nullable=False)

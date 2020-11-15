from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LineBot(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.String(255), primary_key=True)
    choice = db.Column(db.String(255))
    text = db.Column(db.String(255))
    rounds = db.Column(db.Integer)

    db.create_all()

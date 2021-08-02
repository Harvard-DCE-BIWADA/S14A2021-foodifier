from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

Db = SQLAlchemy()


class users(Db.Model):
    # Ref. to table
    __tablename__ = 'users'

    # Class fields match columns
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), nullable=False)
    password = Db.Column(Db.String(64), nullable=False)
    weeklyg = Db.Column(Db.Integer)
    weekly = Db.Column(Db.Integer)
    dailyg = Db.Column(Db.Integer)
    daily = Db.Column(Db.Integer)
    firstlogin = Db.Column(Db.Integer, nullable=True)
    

    # toString
    def toString(self):
        return f'{self.uid} - #{self.username}'

class foods(Db.Model):
    # Ref. to table
    __tablename__ = 'foods'

    fid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    uid = Db.Column(Db.Integer)
    foodname = Db.Column(Db.String(64))
    calorie = Db.Column(Db.Integer)
    date = Db.Column(Db.DateTime, nullable = True, default = datetime.now())




from flask_sqlalchemy import SQLAlchemy

Db = SQLAlchemy()


class User(Db.Model):
    __tablename__ = 'users'
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), unique=True, nullable=False)
    password = Db.Column(Db.String(128), nullable=False)

class UserGoals(Db.Model):
    # Ref. to table
    __tablename__ = 'goals'

    # Class fields match columns
    uid = Db.Column(Db.Integer, primary_key=True)
    weeklyg = Db.Column(Db.Integer)
    weekly = Db.Column(Db.Integer)
    dailyg = Db.Column(Db.Integer)
    daily = Db.Column(Db.Integer)
    
    #age = Db.Column(Db.Integer, nullable=False)
    

    # toString
    def toString(self):
        return f'{self.uid} - #{self.username} ({self.first_name} {self.last_name})'

"""
class Post(Db.Model):
    __tablename__ = 'posts'
    pid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    author = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable=False)
    content = Db.Column(Db.String(1024), nullable=False)
"""
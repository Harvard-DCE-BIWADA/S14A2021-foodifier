from flask_sqlalchemy import SQLAlchemy

# Initialize Db
Db = SQLAlchemy()


class HomeworkUser(Db.Model):
    # Ref. to table
    __tablename__ = 'goals'

    # Class fields match columns
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    weeklyg = Db.Column(Db.Integer, nullable=False)
    weekly = Db.Column(Db.Integer, nullable=False)
    dailyg = Db.Column(Db.Integer, nullable=False)
    daily = Db.Column(Db.Integer, nullable=False)
    
    age = Db.Column(Db.Integer, nullable=False)
    

    # toString
    def toString(self):
        return f'{self.uid} - #{self.username} ({self.first_name} {self.last_name})'

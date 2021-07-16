from flask_sqlalchemy import SQLAlchemy

# Initialize Db
Db = SQLAlchemy()


class HomeworkUser(Db.Model):
    # Ref. to table
    __tablename__ = 'users'

    # Class fields match columns
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), nullable=False)
    password = Db.Column(Db.String(64), nullable=False)
    

    # toString
    def toString(self):
        return f'{self.uid} - #{self.username}'

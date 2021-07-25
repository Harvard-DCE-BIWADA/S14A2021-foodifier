from app import daily_total, weekly_total
import time
from sqlalchemy import update
from sqlalchemy.sql.expression import update
from sqlalchemy.sql.functions import user
from models.models import Db, User, Post, UserGoals, Users

while True:
    time.sleep(86400)
    all_goals=  User.select(User.weeklyg,User.weekly,User.daily,User.daily)
    
    stmt = (
    update(User).
    where(User.uid > 0).
    values(weeklyg='0',weekly='0',daily='0',dailyg='0')
)
    Db.session.add(stmt)
    Db.session.commit



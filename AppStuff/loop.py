from app import daily_total, weekly_total
import time
from sqlalchemy import update
from sqlalchemy.sql.expression import update
from sqlalchemy.sql.functions import user
from models.models import Db, users

while True:
    for x in range(7):
        time.sleep(86400)
        resetd = users(daily=0)
        Db.session.add(resetd)
        Db.session.commit

    resetw = users(weekly=0)
    Db.session.add(resetw)
    Db.session.commit

    





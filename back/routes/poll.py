from fastapi import APIRouter
from config.db import meta
from models.tables import notifications, users, poll
from config.db import conn, meta
from sqlalchemy.sql.expression import delete, join, select, update
from sqlalchemy import exc
from schemas.datatypes import CompleteUser, User, Response

polls = APIRouter()

@polls.get("/poll")
def get_poll():
    return conn.execute(poll.select()).fetchall()

@polls.post("/poll/{label}")
def vote(user: CompleteUser, label: str):
    select_votes_command = select([poll.c.votes]).select_from(poll).where(poll.c.label == label)
    new_votes = {"votes": conn.execute(select_votes_command).fetchone()[0] + 1}
    update_command = update(poll).where(poll.c.label == label).values(new_votes)
    try:
        conn.execute(update_command)
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El poll ya existe"}}
    return {"status": 1, "detail": "ok"}




    
    
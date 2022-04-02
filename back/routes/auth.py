from fastapi import APIRouter
from config.db import meta
from models.tables import notifications, users
from config.db import conn, meta
from sqlalchemy.sql.expression import delete, join, select
from sqlalchemy import exc
from schemas.datatypes import CompleteUser, User, Response, Credentials

login = APIRouter()

@login.post("/login")
def login_post(credentials: Credentials):
    login_command = select([users.c.username]).select_from(users).where((users.c.username == credentials.username) & (users.c.password == credentials.password))
    user = conn.execute(login_command).fetchone()
    if user is None:
        return {"status":-1, "detail":"incorrect username or password"}
    else:
        return {"status":1, "detail": user[0]}
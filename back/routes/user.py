from fastapi import APIRouter
from config.db import meta
from models.tables import notifications, users, suscriptions
from config.db import conn, meta
from sqlalchemy.sql.expression import delete, join, select
from sqlalchemy import exc
from schemas.datatypes import CompleteUser, User, Response

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/user")
def post_user(user: CompleteUser):
    new_user = {
        "username": user.username,
        "password": user.password, # hasheada obveo
        "description": user.description,
        "pictureId": user.pictureId,
        "birthdate": user.birthdate,
        "rank": 0,
        "isVerified": False,
        "email": user.email,
        "website": user.website,
        "linkedin": user.linkedin
    }
    # Insertamos el user en la tabla user.
    try : 
        conn.execute(users.insert().values(new_user))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El usuario ya existe"}}
    return {"status":1, "detail":"ok"}

@user.get("/users/{username}")
def get_userid(username: str):
    select_st = select([users.c.username, users.c.description, users.c.birthdate, users.c.rank, users.c.pictureId, users.c.isVerified, users.c.email, users.c.website, users.c.linkedin]).select_from(users).where(users.c.username == username)
    res = conn.execute(select_st).fetchone()
    return res


@user.post("/suscription/{company_id}")
def user_suscribe(company_id: int, username: str):
    new_suscription = {
        "company_id": company_id,
        "username": username
    }
    try:
        res = conn.execute(suscriptions.insert().values(new_suscription))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El usuario ya esta suscrito"}}
    return {"status":1, "detail":"ok"}
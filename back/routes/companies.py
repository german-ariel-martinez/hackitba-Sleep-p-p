from fastapi import APIRouter
from config.db import meta
from models.tables import notifications, users, companies, ama_posts
from config.db import conn, meta
from sqlalchemy.sql.expression import delete, join, select, update
from sqlalchemy import exc
from schemas.datatypes import CompleteUser, User, Response, AMA_post
from datetime import datetime

company = APIRouter()

@company.get("/companies")
def get_companies():
    return conn.execute(company.select()).fetchall()

@company.get("/companies/{id}")
def get_company(id: int):
    return conn.execute(select([companies.c.name, companies.c.id, companies.c.description]).select_from(companies).where(companies.c.id == id)).fetchone()


@company.get("/companies/{id}/ama")
def get_company_ama(id: int):
    select_st = select([ama_posts.c.threadId]).select_from(ama_posts).where(ama_posts.c.companyId == id).distinct()
    return conn.execute(select_st).fetchall()

@company.post("/companies/{id}/ama")
def post_company_ama(ama_post: AMA_post, id: int):
    new_ama_post = {
        'title': ama_post.title,
        'text': ama_post.text,
        'author': ama_post.author,
        'companyId': id,
        'timestamp': datetime.now(),
        'score': 0
    }
    try : 
        conn.execute(ama_posts.insert().values(new_ama_post))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El post ya existe"}}
    return {"status":1, "detail":"ok"}

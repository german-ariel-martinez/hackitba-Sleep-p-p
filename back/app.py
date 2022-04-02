from fastapi import FastAPI
from routes.user import user
from routes.posts import post
from routes.auth import login

app = FastAPI()

app.include_router(user)
app.include_router(post)
app.include_router(login)

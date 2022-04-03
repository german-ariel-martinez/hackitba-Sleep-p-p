from fastapi import FastAPI
from routes.user import user
from routes.posts import post
from routes.auth import login
from routes.poll import polls
from routes.companies import company
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user)
app.include_router(post)
app.include_router(login)
app.include_router(polls)
app.include_router(company)

origins = ["*", "http://localhost:8080/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

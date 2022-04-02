import datetime

from fastapi import APIRouter
from config.db import meta
from models.tables import notifications, posts, users, comments, threads
from config.db import conn, meta
from sqlalchemy.sql.expression import delete, join, select, update, func
from sqlalchemy import exc
from schemas.datatypes import CompleteUser, User, Response, Post, Comment

post = APIRouter()

UPVOTES_PER_RANK = 10
MIN_RANK_TO_POST = 2

@post.get("/posts")
def get_posts():
    return conn.execute(posts.select()).fetchall()

@post.post("/post")
def post_post(new_post_1: Post):
    author_rank = conn.execute(select([users.c.rank]).select_from(users).where(users.c.username == new_post_1.author)).fetchone()[0]
    if author_rank < MIN_RANK_TO_POST:
        return {"status":-1, "detail":"forbidden"}
    new_post_2 = {
        "title": new_post_1.title,
        "text": new_post_1.text,
        "author": new_post_1.author,
        "timestamp":datetime.datetime.now(),
        "score": 0
    }
    if new_post_1.parentPostId is not None:
        select_parent_post_command = select([posts.c.threadId]).select_from(posts).where(posts.c.id == new_post_1.parentPostId)
        threadId = conn.execute(select_parent_post_command).fetchone()[0]
        if threadId is None:
            new_thread = {'owner': new_post_1.author}
            conn.execute(threads.insert().values(new_thread))
            threadId = conn.execute(select([func.max(threads.c.id)]).select_from(threads).group_by(threads.c.owner)).fetchone()[0]
            new_threadId = {'threadId': threadId}
            conn.execute(update(posts).where(posts.c.id == new_post_1.parentPostId).values(new_threadId))
        new_post_2["threadId"] = threadId

    # Insertamos el post en la tabla posts.
    try : 
        conn.execute(posts.insert().values(new_post_2))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El post ya existe"}}
    # Pedimos el id creado.
    return {"status":1, "detail":"ok"}


@post.post("/post/{postid}/comment")
def comment_post(new_comment: Comment, postid: int):
    new_comment_2 = {
        "author": new_comment.author,
        "text": new_comment.text,
        "postId":  postid,
        "parentId": None,
        "score": 0
    }
    try : 
        conn.execute(comments.insert().values(new_comment_2))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El comment ya existe"}}
    return {"status": 1, "detail": "ok"}

@post.post("/post/{postid}/comment/{commentid}")
def comment_comment(new_comment: Comment, postid: int, commentid: int):
    new_comment_2 = {
        "author": new_comment.author,
        "text": new_comment.text,
        "postId":  postid,
        "parentId": commentid,
        "score": 0
    }
    try : 
        conn.execute(comments.insert().values(new_comment_2))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El comment ya existe"}}
    return {"status": 1, "detail": "ok"}

@post.post("/comment/{commentid}/upvote")
def comment_upvote(commentid: int):
    select_command = select([comments.c.score, comments.c.author]).select_from(comments).where(comments.c.id == commentid)
    new_score_comment, author = conn.execute(select_command).fetchone()
    new_score_comment += 1
    select_post_upvotes_command = select([posts.c.score]).select_from(posts).where(posts.c.author == author)
    select_comment_upvotes_command = select(func.sum(comments.c.score)).select_from(comments).where(comments.c.author == author).group_by(comments.c.author)
    new_score = {"score": new_score_comment}
    try : 
        update_command = update(comments).where(comments.c.id == commentid).values(new_score)
        conn.execute(update_command)
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El comment ya existe"}}

    upvotes = conn.execute(select_comment_upvotes_command).fetchone()[0] + conn.execute(select_post_upvotes_command).fetchone()[0]
    if upvotes % UPVOTES_PER_RANK == 0:
        select_rank = select([users.c.rank]).select_from(users).where(users.c.username == author)
        new_rank = {"rank": conn.execute(select_rank).fetchone()[0] + 1}
        try : 
            update_rank_command = update(users).where(users.c.username == author).values(new_rank)
            conn.execute(update_rank_command)
        except exc.IntegrityError:
            return {"status":-1, "detail":{"error":"El comment ya existe"}}
    return {"status": 1, "detail": "ok"}

@post.post("/comment/{commentid}/downvote")
def comment_downvote(commentid: int):
    select_command = select([comments.c.score, comments.c.author]).select_from(comments).where(comments.c.id == commentid)
    new_score_comment, author = conn.execute(select_command).fetchone()
    new_score_comment -= 1
    select_post_upvotes_command = select([posts.c.score]).select_from(posts).where(posts.c.author == author)
    select_comment_upvotes_command = select(func.sum(comments.c.score)).select_from(comments).where(comments.c.author == author).group_by(comments.c.author)
    new_score = {"score": new_score_comment}
    try : 
        update_command = update(comments).where(comments.c.id == commentid).values(new_score)
        conn.execute(update_command)
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El comment ya existe"}}

    upvotes = conn.execute(select_comment_upvotes_command).fetchone()[0] + conn.execute(select_post_upvotes_command).fetchone()[0]
    if upvotes % UPVOTES_PER_RANK == UPVOTES_PER_RANK - 1:
        select_rank = select([users.c.rank]).select_from(users).where(users.c.username == author)
        new_rank = {"rank": conn.execute(select_rank).fetchone()[0] - 1}
        try : 
            update_rank_command = update(users).where(users.c.username == author).values(new_rank)
            conn.execute(update_rank_command)
        except exc.IntegrityError:
            return {"status":-1, "detail":{"error":"El comment ya existe"}}
    return {"status": 1, "detail": "ok"}

@post.post("/post/{postid}/upvote")
def post_upvote(postid: int):
    select_command = select([posts.c.score, posts.c.author]).select_from(posts).where(posts.c.id == postid)
    new_score_post, author = conn.execute(select_command).fetchone()
    new_score_post += 1
    select_post_upvotes_command = select([posts.c.score]).select_from(posts).where(posts.c.author == author)
    select_comment_upvotes_command = select(func.sum(comments.c.score)).select_from(comments).where(comments.c.author == author).group_by(comments.c.author)
    new_score = {"score": new_score_post}
    try : 
        update_command = update(posts).where(posts.c.id == postid).values(new_score)
        conn.execute(update_command)
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El comment ya existe"}}

    upvotes = conn.execute(select_comment_upvotes_command).fetchone()[0] + conn.execute(select_post_upvotes_command).fetchone()[0]
    if upvotes % UPVOTES_PER_RANK == 0:
        select_rank = select([users.c.rank]).select_from(users).where(users.c.username == author)
        new_rank = {"rank": conn.execute(select_rank).fetchone()[0] + 1}
        try : 
            update_rank_command = update(users).where(users.c.username == author).values(new_rank)
            conn.execute(update_rank_command)
        except exc.IntegrityError:
            return {"status":-1, "detail":{"error":"El comment ya existe"}}
    return {"status": 1, "detail": "ok"}

@post.post("/post/{postid}/downvote")
def post_downvote(postid: int):
    select_command = select([posts.c.score, posts.c.author]).select_from(posts).where(posts.c.id == postid)
    new_score_post, author = conn.execute(select_command).fetchone()
    new_score_post -= 1
    select_post_upvotes_command = select([posts.c.score]).select_from(posts).where(posts.c.author == author)
    select_comment_upvotes_command = select(func.sum(comments.c.score)).select_from(comments).where(comments.c.author == author).group_by(comments.c.author)
    new_score = {"score": new_score_post}
    try : 
        update_command = update(posts).where(posts.c.id == postid).values(new_score)
        conn.execute(update_command)
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El comment ya existe"}}

    upvotes = conn.execute(select_comment_upvotes_command).fetchone()[0] + conn.execute(select_post_upvotes_command).fetchone()[0]
    if upvotes % UPVOTES_PER_RANK == UPVOTES_PER_RANK - 1:
        select_rank = select([users.c.rank]).select_from(users).where(users.c.username == author)
        new_rank = {"rank": conn.execute(select_rank).fetchone()[0] - 1}
        try : 
            update_rank_command = update(users).where(users.c.username == author).values(new_rank)
            conn.execute(update_rank_command)
        except exc.IntegrityError:
            return {"status":-1, "detail":{"error":"El comment ya existe"}}
    return {"status": 1, "detail": "ok"}


from datetime import date, time
from enum import unique
from sqlite3 import Timestamp
from xmlrpc.client import Boolean
from sqlalchemy import Table, Column, engine, Sequence
from sqlalchemy import Table, Column, ForeignKey, text, true
from sqlalchemy.sql.expression import table
from sqlalchemy.sql.sqltypes import TEXT, Date, Integer, String, DateTime, Text, Time, Boolean
from config.db import meta, engine

USER_ID_SEQ = Sequence('user_id_seq')
NOTIFICATIONS_ID_SEQ = Sequence('notifications_id_seq')
PICTURES_ID_SEQ = Sequence('pictures_id_seq')
THREADS_ID_SEQ = Sequence('threads_id_seq')
POSTS_ID_SEQ = Sequence('posts_id_seq')
COMMENTS_ID_SEQ = Sequence('comments_id_seq')
            
pictures = Table("pictures", meta,
            Column("id", Integer, PICTURES_ID_SEQ, primary_key=true, server_default=PICTURES_ID_SEQ.next_value(), unique=true),
            Column("filename", Text, nullable=False),
            Column("picture", Text, nullable=False))

users = Table("users", meta,
            Column("username", Text, nullable=False, primary_key=true, unique=true),
            Column("password", Text, nullable=False),
            Column("description", Text),
            Column("pictureId", Integer, ForeignKey("pictures.id")),
            Column("birthdate", Date, nullable=False),
            Column("rank", Integer, nullable=False, server_default='0'),
            Column("isVerified", Boolean, nullable=False),
            Column("email", Text, nullable=False, unique=true),
            Column("website", Text), 
            Column("linkedin", Text))

notifications = Table("notifications", meta,
                Column("id", Integer, NOTIFICATIONS_ID_SEQ, primary_key=true, server_default=NOTIFICATIONS_ID_SEQ.next_value(), unique=true),
                Column("text", Text, nullable=False),
                Column("userId", Text, ForeignKey("users.username"), nullable=False),
                Column("link", Text))

threads = Table("threads", meta,
            Column("id", Integer, THREADS_ID_SEQ, nullable=False, primary_key=true, server_default=THREADS_ID_SEQ.next_value(), unique=true ),
            Column("owner", Text, ForeignKey("users.username"), nullable=False))
 
posts = Table("posts", meta,
            Column("title", Text, nullable=False),
            Column("text", Text, nullable=False),
            Column("id", Integer, POSTS_ID_SEQ, nullable=False, primary_key=true, server_default=POSTS_ID_SEQ.next_value(), unique=true),
            Column("threadId", Integer, ForeignKey("threads.id")),
            Column("author", Text, ForeignKey("users.username"), nullable=False),
            Column("timestamp", Time, nullable=False),
            Column("threadNumeration", Integer),
            Column("score", Integer))

comments = Table("comments", meta,
            Column("id", Integer, COMMENTS_ID_SEQ, nullable=False, primary_key=true, server_default=COMMENTS_ID_SEQ.next_value(), unique=true),
            Column("author", Text, ForeignKey("users.username"), nullable=False),
            Column("text", Text, nullable=False),            
            Column("postId", Integer, ForeignKey("posts.id"), nullable=False),
            Column("parentId", Integer, ForeignKey("comments.id")),
            Column("score", Integer))

post_labels = Table("postLabels", meta,
            Column("name", Text, nullable=False, primary_key=true, unique=true ),
            Column("postId", Integer, ForeignKey("posts.id"), nullable=False))

attachments = Table("attachments", meta,
            Column("postId", Integer, ForeignKey("posts.id"), nullable=False),
            Column("filename", Text, nullable=False),
            Column("content", Text, nullable=False))

saved_posts = Table("savedPosts", meta,
            Column("postId", Integer, ForeignKey("posts.id"), nullable=False),
            Column("userId", Text, ForeignKey("users.username"), nullable=False))


meta.create_all(engine)
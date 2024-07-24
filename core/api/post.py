from fastapi import APIRouter

from db.queries.post import PostORM
from utils.schemas.post import PostBaseSchema


post_router = APIRouter()


@post_router.get("/posts", response_model=PostBaseSchema)
def get_posts():
    posts = PostORM.get_posts()
    return posts


@post_router.get("/posts/{post_id}", response_model=PostBaseSchema)
def get_post_by_id(post_id: int):
    post = PostORM.get_post_by_id(post_id=post_id)
    return post

from fastapi import APIRouter

from db.queries.comment import CommentORM
from utils.schemas.comment import CommentStartSchema


comment_router = APIRouter()


@comment_router.get("/comments", response_model=CommentStartSchema)
def get_comments():
    comments = CommentORM.get_comments()
    return comments


@comment_router.get("/comments/{comment_id}", response_model=CommentStartSchema)
def get_comment_by_id(comment_id: int):
    comment = CommentORM.get_comment_by_id(comment_id=comment_id)
    return comment

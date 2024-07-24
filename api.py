from typing import List

from fastapi import FastAPI

from db.models.example import Example
from db.models.user import User
from db.models.comment import Comment
from db.models.post import Post
from db.queries.example import ExampleORM
from utils.db.setup import setup_db
from utils.schemas.example import ExampleSchema
from core.api.account import account_router
from core.api.post import post_router
from core.api.comment import comment_router


app = FastAPI()

app.include_router(account_router)
app.include_router(post_router)
app.include_router(comment_router)

setup_db()


@app.get("/example", response_model=List[ExampleSchema])
def example() -> List[Example]:
    return ExampleORM.get_example()

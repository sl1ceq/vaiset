from typing import Optional, List

from .base import VaisetBaseIDSchema
from .comment import Comment
from .post import Post


class User(VaisetBaseIDSchema):
    username: str
    email: str
    password: str
    first_name: Optional[str]
    second_name: Optional[str]
    posts: List[Post]
    comments: List[Comment]

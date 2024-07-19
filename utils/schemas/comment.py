import datetime

from .base import VaisetBaseIDSchema
from .post import Post
from .user import User


class Comment(VaisetBaseIDSchema):
    title: str
    description: str
    created_at: datetime.datetime
    post: Post
    user: User
    # parent_comment треба додати

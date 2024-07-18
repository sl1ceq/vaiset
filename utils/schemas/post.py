from typing import List

from .comment import Comment
from .base import VaisetBaseIDSchema
import datetime

from .user import User


class Post(VaisetBaseIDSchema):
    title: str
    description: str
    created_at: datetime.datetime
    user: User
    comments: List[Comment]

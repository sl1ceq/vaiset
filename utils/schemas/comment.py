from datetime import datetime
from typing import Optional, List

from utils.schemas.base import VaisetBaseIDSchema
from utils.schemas.user import UserBaseSchema
from utils.schemas.post import PostBaseSchema


class CommentStartSchema(VaisetBaseIDSchema):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


class CommentBaseSchema(CommentStartSchema):
    post: Optional[List[PostBaseSchema] | None]
    author: Optional[List[UserBaseSchema] | None]
    parent_comment: Optional[List[CommentStartSchema] | None]
from datetime import datetime
from typing import Optional, List, Union

from db.models.post import PostStatus
from utils.schemas.base import VaisetBaseIDSchema
from utils.schemas.comment import CommentBaseSchema
from utils.schemas.user import UserBaseSchema


class PostBaseSchema(VaisetBaseIDSchema):
    title: str
    description: str
    status: PostStatus
    created_at: datetime
    updated_at: datetime
    author: Optional[UserBaseSchema | None]
    comments: Optional[Union[List[CommentBaseSchema] | CommentBaseSchema] | None]


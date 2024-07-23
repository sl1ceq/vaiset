from datetime import datetime
from typing import Optional, List, Union

from utils.schemas.base import VaisetBaseIDSchema
from utils.schemas.comment import CommentBaseSchema
from utils.schemas.post import PostBaseSchema


class UserBaseSchema(VaisetBaseIDSchema):
    username: str
    email: str
    hashed_password: str
    first_name: Optional[str | None]
    second_name: Optional[str | None]
    created_at: datetime
    updated_at: datetime
    posts: Optional[Union[List[PostBaseSchema] | PostBaseSchema] | None]
    comments: Optional[Union[List[CommentBaseSchema] | CommentBaseSchema] | None]


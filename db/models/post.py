from typing import List

import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import VaisetBaseIDModel
import datetime

from .comment import Comment
from .user import User


class Post(VaisetBaseIDModel):
    __tablename__ = "post"
    title: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(100000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime,
                                                 default=datetime.datetime.now(datetime.UTC),
                                                 nullable=False)
    user: Mapped[User] = relationship("User", back_populates="posts")
    comments: Mapped[List[Comment]] = relationship("Comment", back_populates="post")


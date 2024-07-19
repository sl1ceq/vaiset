from typing import List

import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import VaisetBaseIDModel
from .comment import Comment
from .post import Post


class User(VaisetBaseIDModel):
    __tablename__ = "user"
    username: Mapped[str] = mapped_column(sa.String(20), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(30), nullable=False)
    hashed_password: Mapped[str] = mapped_column(sa.String(24), nullable=False)
    first_name: Mapped[str] = mapped_column(sa.String(20), nullable=True)
    second_name: Mapped[str] = mapped_column(sa.String(20), nullable=True)
    posts: Mapped[List[Post]] = relationship("Post", back_populates="user")
    comments: Mapped[List[Comment]] = relationship("Comment", back_populates="user|")

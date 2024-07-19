import datetime
import sqlalchemy as sa

from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .comment import Comment
from .post import Post
from db.models import base as base_models


class User(base_models.VaisetBaseIDModel):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(
        sa.String(20),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        sa.String(30),
        nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        sa.String(24),
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(
        sa.String(20),
        nullable=True
    )
    second_name: Mapped[str] = mapped_column(
        sa.String(20),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime,
        default=datetime.datetime.now(datetime.UTC),
        nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )
    posts: Mapped[List[Post]] = relationship(
        "Post",
        back_populates="user"
    )
    comments: Mapped[List[Comment]] = relationship(
        "Comment",
        back_populates="user"
    )

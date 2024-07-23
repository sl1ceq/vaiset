import sqlalchemy as sa
import datetime

from typing import List, TYPE_CHECKING
from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models import base as base_models


if TYPE_CHECKING:
    from db.models.comment import Comment
    from db.models.user import User


class PostStatus(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'


class Post(base_models.VaisetBaseIDModel):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(
        sa.String(100),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        sa.String(10000000),
        nullable=False
    )
    status: Mapped[PostStatus] = mapped_column(
        sa.Enum(
            PostStatus, name='post_status'
        )
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
    user_id: Mapped[int] = mapped_column(
        sa.Integer,
        sa.ForeignKey("user.id")
    )
    author: Mapped["User"] = relationship(
        "User",
        back_populates="posts"
    )
    comments: Mapped[List["Comment"]] = relationship(
        "Comment",
        back_populates="post"
    )

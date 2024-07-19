import datetime
import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import VaisetBaseIDModel
from .post import Post
from .user import User
from db.models import base as base_models


class Comment(base_models.VaisetBaseIDModel):
    __tablename__ = "comment"

    title: Mapped[str] = mapped_column(
        sa.String(50),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        sa.String(100000),
        nullable=False
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
    post: Mapped[Post] = relationship(
        "Post",
        back_populates="comments"
    )
    author: Mapped[User] = relationship(
        "User",
        back_populates="comments"
    )
    parent_comment: Mapped["Comment"] = relationship(
        "Comment",
        remote_side=[id],
        back_populates="replies"
    )

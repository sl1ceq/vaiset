import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models import base as base_models


if TYPE_CHECKING:
    from db.models.post import Post
    from db.models.user import User


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
    post_id: Mapped[int] = mapped_column(
        sa.Integer,
        sa.ForeignKey("post.id")
    )
    user_id: Mapped[int] = mapped_column(
        sa.Integer,
        sa.ForeignKey("user.id")
    )
    parent_comment_id: Mapped[int] = mapped_column(
        sa.Integer,
        sa.ForeignKey("comment.id"),
        nullable=True
    )
    post: Mapped["Post"] = relationship(
        "Post",
        back_populates="comments"
    )
    author: Mapped["User"] = relationship(
        "User",
        back_populates="comments"
    )
    parent_comment: Mapped["Comment"] = relationship(
        "Comment",
        remote_side=[id],
        back_populates="replies"
    )

import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import VaisetBaseIDModel

import datetime

from .post import Post
from .user import User


class Comment(VaisetBaseIDModel):
    __tablename__ = "comment"
    title: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(100000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime,
                                                 default=datetime.datetime.now(datetime.UTC),
                                                 nullable=False)
    post: Mapped[Post] = relationship("Post", back_populates="comments")
    user: Mapped[User] = relationship("User", back_populates="comments")
    #parent_comment треба додати

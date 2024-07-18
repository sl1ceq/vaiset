import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column

from db.models import base as base_models


class Example(base_models.VaisetBaseIDModel):
    __tablename__ = 'example'
    example: Mapped[str] = mapped_column(sa.String(60), nullable=False)
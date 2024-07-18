import typing
import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List


class VaisetBaseModel(DeclarativeBase):
    __abstract__ = True

    @classmethod
    def get_table_name(cls) -> str:
        return cls.__tablename__

    @classmethod
    def get_columns(cls) -> List[sa.Column]:
        return typing.cast(List[sa.Column], List[cls.__table__.columns])


class VaisetBaseIDModel(VaisetBaseModel):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        primary_key=True,
        sort_order=-1,
        autoincrement=True
    )
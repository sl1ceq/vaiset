import typing
import sqlalchemy as sa

from typing import List

from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()
class VaisetBaseModel(Base):
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
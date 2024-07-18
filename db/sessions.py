import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from db.models.base import VaisetBaseModel

SQLITE_URL = "sqlite:///test.db"

engine = sa.create_engine(SQLITE_URL, echo=True)
Session = sessionmaker(bind=engine)
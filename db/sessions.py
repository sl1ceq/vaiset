import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


SQLITE_URL = "sqlite:///test_for_vaiset_1.db"

engine = sa.create_engine(SQLITE_URL, echo=True)
Session = sessionmaker(bind=engine)
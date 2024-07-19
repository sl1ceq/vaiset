from db.models.base import VaisetBaseIDModel
from db.sessions import engine


def setup_db():
    VaisetBaseIDModel.metadata.create_all(engine)
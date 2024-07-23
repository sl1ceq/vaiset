from db.models import base as base_models
from db.sessions import engine


def setup_db():
    base_models.VaisetBaseIDModel.metadata.create_all(bind=engine)

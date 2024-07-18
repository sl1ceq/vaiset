from db.models.base import VaisetBaseModel
from db.sessions import engine

BaseModel = VaisetBaseModel


def setup_db():
    BaseModel.metadata.create_all(engine)
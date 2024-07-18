from abc import ABC

from pydantic import BaseModel


class VaisetBaseIDSchema(BaseModel, ABC):
    id: int


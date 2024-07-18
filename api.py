from typing import List

from fastapi import FastAPI

from db.models.example import Example
from db.queries.example import ExampleORM
from utils.db.setup import setup_db
from utils.schemas.example import ExampleSchema

app = FastAPI()

setup_db()


@app.get("/example", response_model=List[ExampleSchema])
def example() -> List[Example]:
    return ExampleORM.get_example()
from typing import List

from db.models.example import Example
from db.sessions import Session


class ExampleORM:

    @staticmethod
    def get_example() -> List[Example]:
        with Session() as session:
            examples = session.query(Example).all()
            return examples

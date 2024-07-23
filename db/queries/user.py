from typing import List

from sqlalchemy import update

from db.models.user import User
from db.sessions import Session


class UserORM:

    @staticmethod
    def get_users() -> List[User]:
        with Session() as session:
            users = session.query(User).all()
            return users

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        with Session() as session:
            user = session.query(User).filter_by(User.id == user_id).first()
            return user

    @staticmethod
    def create_user(data: dict) -> User:
        new_user = User(**data)
        with Session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user

    @staticmethod
    def delete_user(user_id: int) -> User:
        with Session() as session:
            user = session.query(User).filter_by(User.id == user_id).first()
            session.delete(user)
            session.commit()
            return user

    @staticmethod
    def update_user(user_id: int, new_data: dict) -> User:
        with Session() as session:
            data_to_update = update(User).where(User.id == user_id).values(new_data)
            session.execute(data_to_update)
            session.commit()
            updated_user = session.query(User).filter_by(User.id == user_id).first()
            session.refresh(updated_user)
            return updated_user

from typing import List

from sqlalchemy import update

from db.models.post import Post
from db.sessions import Session



class PostORM:

    @staticmethod
    def get_posts() -> List[Post]:
        with Session() as session:
            posts = session.query(Post).all()
            return posts

    @staticmethod
    def get_post_by_id(post_id: int) -> Post:
        with Session() as session:
            post = session.query(Post).filter_by(Post.id == post_id).first()
            return post

    @staticmethod
    def create_post(payload: dict) -> Post:
        new_post = Post(**payload)
        with Session() as session:
            session.add(new_post)
            session.commit()
            session.refresh(new_post)
            return new_post

    @staticmethod
    def delete_post(post_id: int) -> Post:
        with Session() as session:
            post = session.query(Post).filter_by(Post.id == post_id).first()
            session.delete(post)
            session.commit()
            return post

    @staticmethod
    def update_user(post_id: int, payload: dict) -> Post:
        with Session() as session:
            data_to_update = update(Post).where(Post.id == post_id).values(payload)
            session.execute(data_to_update)
            session.commit()
            updated_post = session.query(Post).filter_by(Post.id == post_id).first()
            session.refresh(updated_post)
            return updated_post

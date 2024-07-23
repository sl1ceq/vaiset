from typing import List
from db.models.comment import Comment
from db.sessions import Session
from sqlalchemy import update


class CommentORM:

    @staticmethod
    def get_comments() -> List[Comment]:
        with Session() as session:
            comments = session.query(Comment).all()
            return comments

    @staticmethod
    def get_comment_by_id(comment_id: int) -> Comment:
        with Session() as session:
            comment = session.query(Comment).filter_by(Comment.id == comment_id).first()
            return comment

    @staticmethod
    def create_comment(data: dict) -> Comment:
        new_comment = Comment(**data)
        with Session() as session:
            session.add(new_comment)
            session.commit()
            session.refresh(new_comment)
            return new_comment

    @staticmethod
    def delete_comment(comment_id: int):
        with Session() as session:
            comment = session.query(Comment).filter_by(Comment.id == comment_id).first()
            session.delete(comment)
            session.commit()
            return comment

    @staticmethod
    def update_comment(comment_id: int, new_data: dict) -> Comment:
        with Session() as session:
            data_to_update = update(Comment).where(Comment.id == comment_id).values(new_data)
            session.execute(data_to_update)
            session.commit()
            updated_comment = session.query(Comment).filter_by(Comment.id == comment_id).first()
            session.refresh(updated_comment)
            return updated_comment

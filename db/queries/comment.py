from typing import List

from sqlalchemy import update
from sqlalchemy.orm import joinedload

from db.models.comment import Comment
from db.sessions import Session


class CommentORM:

    @staticmethod
    def get_comments() -> List[Comment]:
        with Session() as session:
            comments = session.query(Comment).options(
                joinedload(Comment.author),
                joinedload(Comment.parent_comment),
                joinedload(Comment.post)
            ).all()
            return comments

    @staticmethod
    def get_comment_by_id(comment_id: int) -> Comment:
        with Session() as session:
            comment = session.query(Comment).options(
                joinedload(Comment.author),
                joinedload(Comment.parent_comment),
                joinedload(Comment.post)
            ).filter(
                Comment.id == comment_id
            ).first()
            return comment

    @staticmethod
    def create_comment(payload: dict) -> Comment:
        new_comment = Comment(**payload)
        with Session() as session:
            session.add(new_comment)
            session.commit()
            session.refresh(new_comment)
            return new_comment

    @staticmethod
    def delete_comment(comment_id: int) -> Comment:
        with Session() as session:
            comment = session.query(Comment).filter_by(Comment.id == comment_id).first()
            session.delete(comment)
            session.commit()
            session.refresh(comment)
            return comment

    @staticmethod
    def update_comment(comment_id: int, payload: dict) -> Comment:
        with Session() as session:
            data_to_update = update(Comment).where(Comment.id == comment_id).values(payload)
            session.execute(data_to_update)
            session.commit()
            updated_comment = session.query(Comment).filter_by(Comment.id == comment_id).first()
            session.refresh(updated_comment)
            return updated_comment

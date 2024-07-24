from fastapi import APIRouter

from db.queries.user import UserORM
from utils.schemas.user import UserBaseSchema


account_router = APIRouter()


@account_router.get("/users", response_model=UserBaseSchema)
def get_accounts():
    accounts = UserORM.get_users()
    return accounts


@account_router.get("/users/{user_id}", response_model=UserBaseSchema)
def get_account_by_id(user_id: int):
    user = UserORM.get_user_by_id(user_id=user_id)
    return user

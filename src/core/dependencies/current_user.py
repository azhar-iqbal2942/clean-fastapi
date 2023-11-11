from fastapi import Depends, Request
from app.handlers.user import UserHandler


def get_current_user(
    request: Request, user_handler: UserHandler = Depends(UserHandler)
):
    print("User ID => ", request.user.id)
    return user_handler.handle_get_user_by_id(request.user.id)

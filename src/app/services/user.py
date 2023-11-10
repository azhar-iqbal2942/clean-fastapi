from app.repositories.user import UserRepository


class UserService:
    def get_all_users(self, session):
        resp = UserRepository().get_all(session=session)
        return resp

    def create_user(self, session, user):
        resp = UserRepository().create(session=session, user=user)
        return resp

    def get_user_by_email(self, session, email):
        resp = UserRepository().get_by_email(session, email)
        return resp

from models.user import User


class UserService:
    def __init__(self, user_queries):
        self.user_queries = user_queries

    def get_all_users(self):
        records = self.user_queries.fetch_user_credentials()
        return [User(email, password) for email, password in records]

from models.user import User
from utils.error_handler import QueryError


class UserService:
    def __init__(self, user_queries):
        self.user_queries = user_queries

    def get_all_users(self):
        records = self.user_queries.fetch_user_credentials()
        return [User(email, password) for email, password in records]

    def authenticate_user(self, email, password):
        try:
            # Buscar al usuario con el email proporcionado
            user_record = self.user_queries.fetch_user_by_email(email)
            if not user_record:
                return False

            # Verificar si la contraseña proporcionada coincide
            stored_password = user_record[1]
            return password == stored_password
        except QueryError as e:
            raise e

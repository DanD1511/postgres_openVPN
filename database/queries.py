import psycopg2

from utils.error_handler import QueryError


class UserQueries:
    def __init__(self, connection):
        self.connection = connection

    def fetch_user_credentials(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT email, "DigSilentPassword" FROM auth_user;')
            return cursor.fetchall()
        except psycopg2.Error as e:
            raise QueryError(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()

import psycopg2

from utils.error_handler import ConnectionDBError


class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return self.connection
        except psycopg2.OperationalError as e:
            raise ConnectionDBError(f"Error de conexión: {e}")

    def close(self):
        if self.connection:
            self.connection.close()

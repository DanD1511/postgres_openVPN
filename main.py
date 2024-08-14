from database.connection import DatabaseConnection
from database.queries import UserQueries
from datasource.db_datasource import DBConfig
from services.user_service import UserService
from utils.error_handler import QueryError, ConnectionDBError


def main():
    db_config = DBConfig()
    db_conn = DatabaseConnection(
        dbname=db_config.dbname,
        user=db_config.user,
        password=db_config.password,
        host=db_config.host,
        port=db_config.port
    )

    try:
        connection = db_conn.connect()
        user_queries = UserQueries(connection)
        user_service = UserService(user_queries)

        # Obtener y mostrar todos los usuarios
        users = user_service.get_all_users()
        for user in users:
            print(f"Email: {user.email}, Password: {user.dig_silent_password}")

    except ConnectionDBError as ce:
        print(ce)

    except QueryError as qe:
        print(qe)

    finally:
        db_conn.close()


if __name__ == "__main__":
    main()

import sys
from PyQt6.QtWidgets import QApplication
from database.connection import DatabaseConnection
from database.queries import UserQueries
from services.user_service import UserService
from ui.login_window import LoginWindow


def main():
    # Configuración de la conexión a la base de datos
    db_conn = DatabaseConnection(
        dbname="ECS",
        user="postgres",
        password="0129",
        host="localhost",
        port="5432"
    )

    try:
        connection = db_conn.connect()
        user_queries = UserQueries(connection)
        user_service = UserService(user_queries)

        # Inicialización de la aplicación PyQt6
        app = QApplication(sys.argv)
        login_window = LoginWindow(user_service)
        login_window.show()

        sys.exit(app.exec())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        db_conn.close()


if __name__ == "__main__":
    main()

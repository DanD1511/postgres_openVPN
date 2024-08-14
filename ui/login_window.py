from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from services.user_service import UserService


class LoginWindow(QWidget):
    def __init__(self, user_service):
        super().__init__()

        self.user_service = user_service

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 280, 150)

        layout = QVBoxLayout()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.authenticate_user)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def authenticate_user(self):
        email = self.email_input.text()
        password = self.password_input.text()

        try:
            if self.user_service.authenticate_user(email, password):
                QMessageBox.information(self, "Success", "Login Successful")
                # Aquí puedes avanzar a la siguiente ventana o funcionalidad
            else:
                QMessageBox.warning(self, "Error", "Invalid credentials")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

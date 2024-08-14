from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.welcome_label = QLabel(f"Welcome, {user.email}")
        layout.addWidget(self.welcome_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

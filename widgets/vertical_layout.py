import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
)


# Подкласс QMainWindow для настройки основного окна приложения
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # add widgets to the layout
        layout.addWidget(QPushButton("Top Button"))
        layout.addWidget(QPushButton("Middle Button"))
        layout.addWidget(QPushButton("Bottom Button"))
        # Set the layout on the application window
        self.setLayout(layout)


if __name__ == "__main__":
    # Создание приложения Qt
    app = QApplication(sys.argv)

    # Создание основного окна
    window = MainWindow()
    window.show()

    # Запуск основного цикла Qt
    sys.exit(app.exec())

# The code creates a simple GUI application using PyQt6 that demonstrates the use of QHBoxLayout to arrange buttons in a horizontal layout.
# The application consists of a main window with three buttons arranged from left to right. 

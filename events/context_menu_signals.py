import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse context menu Demo")
        self.setFixedSize(QSize(400, 300))
        self.label = QLabel("Right Click in this window")
        self.setCentralWidget(self.label)
        
        self.show()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # Connect the signal
        self.customContextMenuRequested.connect(self.on_context_menu)


    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

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

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("Context menu item 1", self))
        context.addAction(QAction("Context menu item 2", self))
        context.addAction(QAction("Context menu item 3", self))
        context.exec(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

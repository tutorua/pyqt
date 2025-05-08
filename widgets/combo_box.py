import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout, QGridLayout, QFormLayout,
    QTabWidget, QStackedWidget, QScrollArea, QSpacerItem,
    QSizePolicy, QLineEdit, QDateEdit, QTimeEdit, QDateTimeEdit,
    QDial, QLCDNumber, QProgressBar, QFontComboBox, QCheckBox,
    QRadioButton, QSlider, QSpinBox, QDoubleSpinBox,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Test generator")
        # self.setGeometry(50, 50, 400, 200)

        
        layout = QVBoxLayout()
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        layout.addWidget(widget)

        # Отправляет текущий индекс (позицию) выбранного элемента.
        widget.currentIndexChanged.connect(self.index_changed)

        # Есть альтернативный сигнал отправки текста.
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)


    def index_changed(self, i): # i — это int
        print(i)

    def text_changed(self, s): # s — это str
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
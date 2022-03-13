import sys
from PyQt6.QtCore import QSize, Qt
import PyQt6.QtWidgets
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
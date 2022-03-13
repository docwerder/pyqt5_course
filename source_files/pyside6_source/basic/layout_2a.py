import sys

from PySide6.QtCore import Qt
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QSpinBox, QLabel
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        #layout.addWidget(QLabel('Label 1'))
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("yellow"))
        print('tyep: ', type(Color("red")))
        #layout.addWidget(QLabel(), 0, QtCore.Qt.Alignment())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

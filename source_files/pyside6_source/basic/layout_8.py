import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.layoutColumnStretch(1,1,1)
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn_red = QPushButton("red")
        btn_red.clicked.connect(self.activate_tab_1)
        button_layout.addWidget(btn_red)
        self.stacklayout.addWidget(Color("red"))

        btn_green = QPushButton("green")
        btn_green.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn_green)
        self.stacklayout.addWidget(Color("green"))

        btn_yellow = QPushButton("yellow")
        btn_yellow.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn_yellow)
        self.stacklayout.addWidget(QLabel('Hallo welt'))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


if __name__== '__main__':
    app = QApplication(sys.argv)
    print(sys.path)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

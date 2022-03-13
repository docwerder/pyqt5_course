import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            print('n: ', n)
            print('color: ', color)
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

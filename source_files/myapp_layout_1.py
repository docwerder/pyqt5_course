import sys
sys.path.append('/Users/joerg/repos')
from PyQt6.QtCore import QSize, Qt
import PyQt6.QtWidgets
from PySide6.QtWidgets import \
    QApplication, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QMainWindow
from pyside6_source.basic.layout_colorwidget import Color #as COlor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 1)
        layout.addWidget(Color("yellow"), 2, 0)
        layout.addWidget(Color("green"), 3, 1)


        btn_layout = QHBoxLayout()
        btn_layout.addWidget(QPushButton('BTN 1'))
        btn_layout.addWidget(QPushButton('BTN 2'))

        layout_all = QVBoxLayout()
        layout_all.addLayout(layout)
        layout_all.addLayout(btn_layout)

        widget = QWidget()
        widget.setLayout(layout_all)
        self.setCentralWidget(widget)
        # btn_layout.addWidget(QLabel('Label 2'))
        # color_layout.addWidget(COlor("red"))

        #my_layout.addWidget(Color("red"))

        # dummy_widget = QWidget()
        # dummy_widget.setLayout(color_layout)
        # self.setCentralWidget(dummy_widget)
        # Set the central widget of the Window.
        #self.setCentralWidget(self.button)

if __name__== '__main__':
    app = QApplication(sys.argv)
    print(sys.path)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

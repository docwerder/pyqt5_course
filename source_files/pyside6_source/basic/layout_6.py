import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QPushButton
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        unicode_character = "\u00A9 "
        print(unicode_character)
        title_text = "My App " + unicode_character + "Jörg Wingbermühle"
        self.setWindowTitle(title_text)

        layout = QGridLayout()
        layout.addWidget(QPushButton('BTN1'), 0, 0)

        #layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("yellow"), 0, 1)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("pink"), 2, 0)
        layout.addWidget(Color("purple"), 2, 1)


        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 5)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        font = widget.font()  # <1>
        font.setPointSize(230)
        widget.setFont(QFont("Monaco", 230))#font)

        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # <2>

        self.setCentralWidget(widget)


if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

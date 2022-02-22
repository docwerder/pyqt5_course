import sys
from PyQt6.QtCore import QSize, Qt
import PyQt6.QtWidgets
from PyQt6.QtWidgets import * # QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window class MainWindow(QMainWindow):

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.setMinimumSize(QSize(400, 300))
        self.button.clicked.connect(self.button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        print('button_was_clicked')

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

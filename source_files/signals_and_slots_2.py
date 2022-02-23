import sys
from PyQt6.QtCore import QSize, Qt
import PyQt6.QtWidgets
from PyQt6.QtWidgets import * # QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window class MainWindow(QMainWindow):

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App 1")
        self.button = QPushButton("Press Me!")
        self.setMinimumSize(QSize(400, 300))
        self.button.setCheckable(True)
        self.button_is_checked = True

        self.button.clicked.connect(self.button_was_clicked)
        self.button.clicked.connect(self.button_was_toggled)
        self.button.setChecked(self.button_is_checked)


        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        self.button.setText('You already clicked the button!')
        self.button.setEnabled(False)
        self.setWindowTitle('My Oneshot App')

    def button_was_toggled(self, checked):
        print('Checked? ', checked)
        self.button_is_checked = checked
        print('state of button checked? ', self.button_is_checked)

    def button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print('button? ', self.button_is_checked)


if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

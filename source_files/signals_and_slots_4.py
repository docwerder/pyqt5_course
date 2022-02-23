import sys
from PyQt6.QtCore import QSize, Qt
import PyQt6.QtWidgets
from random import choice
from PyQt6.QtWidgets import * # QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window class MainWindow(QMainWindow):

window_titles = ['My App', 'My App', 'Still My App', 'Still My App',
                 'What on earth', 'What on earth', 'This is surprising',
                 'This is surprising', 'Something went wrong'
                 ]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.label)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        # Old stuff from the former files...
        # self.button.setCheckable(True)
        # self.button_is_checked = True
        # self.button.clicked.connect(self.button_was_toggled)
        # self.button.setChecked(self.button_is_checked)


        # Set the central widget of the Window.


    def button_was_clicked(self):
        self.setWindowTitle('My Oneshot App')
        new_window_title = choice(window_titles)
        print("Setting new WindowTitle: ", new_window_title)
        self.setWindowTitle(new_window_title)


    def the_window_title_changed(self, windowTitle):
        print("Current WindowTitle: ", windowTitle)
        if windowTitle == "Something went wrong":
            self.button.setDisabled(True)

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

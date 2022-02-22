from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QStyleFactory
print(QStyleFactory.keys())
import sys
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('test.ui', self)
        self.setWindowTitle('First Style')

        # Show Window
        self.show()


# os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "-10"
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Plastique")
    window = Ui()
    sys.exit(app.exec())
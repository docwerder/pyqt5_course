import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *

class DlgMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)
        self.ledText = QLineEdit("My GUI", self)
        self.ledText.move(45, 50)

        self.btnUpdate = QPushButton("Update Window Title", self)
        self.btnUpdate.move(35, 80)
        self.btnUpdate.clicked.connect(self.evt_btnUpdate_clicked)

    def evt_btnUpdate_clicked(self):
        self.setWindowTitle(self.ledText.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    app.setStyle('Oxygen')
    print(PyQt5.QtWidgets.QStyleFactory.keys())
    sys.exit(app.exec_())
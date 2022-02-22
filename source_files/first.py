import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
dlgMain = QDialog()
dlgMain.setWindowTitle("My GUI")
dlgMain.show()
app.setStyle('Macintosh')

sys.exit(app.exec_())
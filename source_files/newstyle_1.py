import sys
import os
from PyQt5.QtWidgets import *
from PyQt6.QtCore import QSize, Qt
from PyQt5.QtGui import *

# Create a custom "QProxyStyle" to enlarge the QMenu icons
#-----------------------------------------------------------
class MyProxyStyle(QProxyStyle):
    pass
    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):

        if QStyle_PixelMetric == QStyle.PM_SmallIconSize:
            return 40
        else:
            return QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)


# This is the main window class (with a simple QMenu implemented)
# ------------------------------------------------------------------
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300))   # Set the central widget of the Window. self.setCentralWidget(button)

        # 4. Show the window.
        self.show()

# Start your Qt application based on the new style
#---------------------------------------------------
if __name__== '__main__':
    app = QApplication(sys.argv)
    myStyle = MyProxyStyle('Fusion')    # The proxy style should be based on an existing style,
                                        # like 'Windows', 'Motif', 'Plastique', 'Fusion', ...
    app.setStyle(myStyle)

    myGUI = TestWindow()

    sys.exit(app.exec_())
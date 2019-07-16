from test.MapTest import MapTest
from test.ShootTest import ShootTest

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QPen
from PyQt5.QtCore import Qt

import sys

from view.MainWindow import MainWindow


def tests():
    MapTest()
    ShootTest()
    
if __name__ == "__main__":
    tests()

    app = QApplication(sys.argv)
    run = MainWindow()
    sys.exit(app.exec_())
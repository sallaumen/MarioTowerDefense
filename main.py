import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QPen
from PyQt5.QtCore import Qt

from test.MapTest import MapTest
from test.ShootTest import ShootTest
from controller.gameController import GameController


def tests():
    MapTest()
    ShootTest()
    
if __name__ == "__main__":
    tests()
    app = QApplication(sys.argv)
    run = GameController()
    sys.exit(app.exec_())
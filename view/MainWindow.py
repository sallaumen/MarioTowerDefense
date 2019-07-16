from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt


from model.Map import Map
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Mario Tower Defense'
        self.left = 150
        self.top = 150
        self.width = 900
        self.height = 900
        self.initUI()
        
    

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top,self.width, self.height)

        self.show()
    

    def updateUI(self):
        pass


    def paintEvent(self, e):

        map = Map()
        print(map.get_map())

        self.pintarMapa(map)


    def pintarMapa(self, map):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,  1, Qt.SolidLine))
        
        y = 0

        map_array = map.get_map()

        for linha in map_array:
            x = 0
            for square in linha:
                if square == map.GRASS:
                    painter.setBrush(QBrush(QColor.fromRgbF(0.2, 0.8, 0.5, 1), Qt.Dense1Pattern))
                    painter.drawRect(x, y, 30, 30)
                
                elif square == map.FLOOR:
                    painter.setBrush(QBrush(Qt.brown, Qt.SolidPattern))
                    painter.drawRect(x, y, 30, 30)

                x += 30
            y += 30
            
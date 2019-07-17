from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from model.Player import Player
from model.Map import Map
import sys


class MainWindow(QMainWindow):

    def __init__(self, player):
        super().__init__()
        self.title = 'Mario Tower Defense'
        self.left = 150
        self.top = 150
        self.width = 600
        self.height = 625
        self.initUI(player)
        self.clock_counter = 0

    def initUI(self, player):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top,self.width, self.height)

        y_header = 10

        lbl_player_name = QLabel("Player Name: {}".format(player.get_player_name()), self)
        #lbl_player_name.setFont(QFont.setBold(True))
        lbl_player_name.move(10, y_header)
        lbl_player_name.resize(225, 15)

        lbl_player_life = QLabel("Player Life: {}".format(player.get_player_life()), self)
        lbl_player_life.move(250, y_header)
        lbl_player_life.resize(110, 15)

        lbl_player_money = QLabel("Player Money: {}".format(player.get_player_money()), self)
        lbl_player_money.move(375, y_header)
        lbl_player_money.resize(225, 15)

        self.show()

    def updateUI(self):
        #print(self.clock_counter)
        self.clock_counter += 1

    def paintEvent(self, e):
        map = Map()
        map.create_level_floor()
        self.pintarMapa(map)

    def pintarMapa(self, map):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,  1, Qt.SolidLine))
        block_size = self.width / 30

        y = 25
        map_array = map.get_map()

        for linha in map_array:
            x = 0
            for square in linha:
                if square == map.GRASS:
                    painter.setBrush(QBrush(QColor.fromRgbF(0.2, 0.8, 0.5, 1), Qt.Dense1Pattern))
                    painter.drawRect(x, y, block_size, block_size)
                
                elif square == map.FLOOR:
                    painter.setBrush(QBrush(QColor.fromRgbF(0.7, 0.5, 0.3, 1), Qt.SolidPattern))
                    painter.drawRect(x, y, block_size, block_size)
                x += block_size
            y += block_size

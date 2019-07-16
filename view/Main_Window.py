from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

import sys


class Window(QMainWindow):

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = Window()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

class Window(QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle('Mario Tower Defense')
        self.resize(900, 900)


        self.label = QLabel('Hello World!')
        self.label.show()




root = QApplication(sys.argv)

app = Window()
app.show()

sys.exit(root.exec_())

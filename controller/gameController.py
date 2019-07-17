from model.Player import Player
from view.MainWindow import MainWindow
from time import sleep
from PyQt5.QtCore import QTimer, QBasicTimer  # Import new bits needed

class GameController:

    FPS = 30
    REFRESH_RATE = (1/FPS)*1000

    def __init__(self):
        self.fps = 60
        self.towers_position = []
        self.enemies_positions = []
        self.game_player = Player("Player 1", 0, 100)
        self.main_window = MainWindow(self.game_player)
        self.timer = QTimer()
        self.timer.timeout.connect(self.main_window.updateUI)
        self.timer.start(self.REFRESH_RATE)
        self.start_game()
        
    def start_game(self):
        pass

    def create_test_game(self):
        pass

    def generate_enemy(self):
        pass
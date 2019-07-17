import numpy as np

class Map:
    GRASS = 0
    FLOOR = 1
    START_GAME = 2
    END_GAME = 3

    def __init__(self):
        self.lenght = 900
        self.width = 900
        self.floor_data = []
        self.create_empty_map()
        self.__game_level = 1

    def create_empty_map(self):
        self.floor_data = np.zeros((30, 30))

    def get_map(self):
        return self.floor_data

    def change_map_size(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def create_level_design(self):
        self.create_level_floor()

    def __create_start(self):
        self.floor_data[29][3] = 1

    def create_level_floor(self):
        if self.__game_level == 1:
            # andar pra cima
            y_mov_1 = 27
            x_mov_1 = 12
            left_margin = 3

            for i in range(y_mov_1):
                self.floor_data[1 + y_mov_1 - i][left_margin] = self.FLOOR
            # andar pra direita
            for i in range(x_mov_1):
                self.floor_data[1][i + left_margin] = self.FLOOR
            # andar pra baixo
            for i in range(y_mov_1):
                self.floor_data[1 + i][x_mov_1 + left_margin] = self.FLOOR
            # andar pra direita
            for i in range(x_mov_1):
                self.floor_data[1 + y_mov_1][x_mov_1 + i + left_margin] = self.FLOOR
            # andar pra cima
            for i in range(y_mov_1):
                self.floor_data[1 + i][x_mov_1 * 2 + left_margin-1] = self.FLOOR

    def set_game_level(self, game_level):
        self.__game_level = game_level
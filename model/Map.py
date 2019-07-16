import numpy as np

class Map:
    GRASS = 0
    FLOOR = 1

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

    def create_one_floor(self, pos_x, pos_y):
        self.floor_data[pos_x][pos_y] = self.FLOOR

    def create_level_floor(self):
        if self.__game_level == 1:
            # andar pra cima
            y_mov_1 = 28
            for i in range(y_mov_1):
                self.floor_data[1][1 + y_mov_1 - i] = self.FLOOR
            # andar pra direita
            x_mov_1 = 12
            for i in range(x_mov_1):
                self.floor_data[i + 1][1] = self.FLOOR
            # andar pra baixo
            for i in range(y_mov_1):
                self.floor_data[x_mov_1 + 1][1 + i] = self.FLOOR
            # andar pra direita
            for i in range(x_mov_1):
                self.floor_data[x_mov_1 + i + 1][1 + y_mov_1] = self.FLOOR
            # andar pra cima
            for i in range(y_mov_1):
                self.floor_data[1 + x_mov_1 * 2][1 + i] = self.FLOOR


    def set_game_level(self, game_level):
        self.__game_level = game_level
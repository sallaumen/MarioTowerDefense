import numpy as np

class Map:
    GRASS = 0
    FLOOR = 1

    def __init__(self):
        self.lenght = 900
        self.width = 900
        self.floor_data = []
        self.create_empty_map()

    def create_empty_map(self):
        self.floor_data = np.zeros((30, 30))

    def get_map(self):
        return self.floor_data

    def change_map_size(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def create_one_floor(self, pos_x, pos_y):
        self.floor_data[pos_x][pos_y] = self.FLOOR

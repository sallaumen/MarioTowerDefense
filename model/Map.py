class Map:
    GRASS = 0
    FLOOR = 1

    def __init__(self):
        self.lenght = 900
        self.width = 900
        self.floor_type = [[-1] * 30]*30
        self.create_empty_map()

    def create_empty_map(self):
        for i in range(0, 30):
            for j in range(0, 30):
                self.floor_type[i][j] = self.GRASS

    def get_map(self):
        return self.floor_type

    def change_map_size(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def create_one_floor(self, pos_x, pos_y):
        self.floor_type[pos_x][pos_y] = self.FLOOR

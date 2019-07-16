class Enemy:

    def __init__(self, life, damage):
        self.__life = life
        self.__position_x = 0
        self.__position_y = 900
        self.__damage = damage
        self.__walk_state = 0
        self.__walk_path_x = []
        self.__walk_path_y = []
        self.__make_walk_path()

    def __make_walk_path(self):
        # andar pra cima
        y_mov_1 = 700
        for i in range(y_mov_1):
            self.__position_x = 0
            self.__position_y = 900 - i
        # andar pra direita
        x_mov_1 = 400
        for i in range(x_mov_1):
            self.__position_x = i
            self.__position_y = y_mov_1
        # andar pra baixo
        for i in range(y_mov_1):
            self.__position_x = x_mov_1
            self.__position_y = y_mov_1 - i
        # andar pra direita
        for i in range(x_mov_1):
            self.__position_x = x_mov_1 + i
            self.__position_y = 0
        # andar pra cima
        for i in range(y_mov_1):
            self.__position_x = x_mov_1 * 2
            self.__position_y = i

    def make_enemy_walk(self):
        self.__position_x = self.__walk_path_x[self.__walk_state]
        self.__position_y = self.__walk_path_y[self.__walk_state]
        self.__walk_state += 1
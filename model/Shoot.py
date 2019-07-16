class Shoot:
    def __init__(self):
        self.bullet_lifetime = 0
        self.position_x = 0
        self.position_y = 0

    def make_a_shoot(self, pos_x, pos_y):
        self.position_x = pos_x
        self.position_y = pos_y

    def get_bullet_position(self):
        return self.position_x, self.position_y
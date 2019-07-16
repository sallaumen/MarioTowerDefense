from model.Shoot import Shoot

class ShootTest:
    def __init__(self):
        self.test_making_a_shoot()

    def test_making_a_shoot(self):
        shoot = Shoot()
        shoot.make_a_shoot(50, 30)
        bullet_position_x, bullet_position_y = shoot.get_bullet_position()
        assert bullet_position_x == 50
        assert bullet_position_y == 30
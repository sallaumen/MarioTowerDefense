from model.Map import Map

class MapTest:

    def __init__(self):
        self.test_map_creation()
        self.test_map_create_floor()
        self.test_create_level_floor()

    def test_map_creation(self):
        map = Map()
        map.create_empty_map()
        get_map = map.get_map()
        for i in range(30):
            for j in range(30):
                assert get_map[i][j] == 0


    def test_map_create_floor(self):
        map = Map()
        map.create_empty_map()
        map.create_one_floor(29, 1)
        get_map = map.get_map()
        assert get_map[29][1] == 1

    def test_create_level_floor(self):
        map = Map()
        map.create_empty_map()
        get_map = map.get_map()
        map.create_level_floor()
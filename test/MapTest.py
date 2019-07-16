from model.Map import Map

class MapTest:

    def __init__(self):
        #self.test_map_creation()
        self.test_map_create_floor()
    def test_map_creation(self):
        map = Map()
        map.create_empty_map()
        get_map = map.get_map()
        for i in get_map:
            print(i)

    def test_map_create_floor(self):
        map = Map()
        map.create_empty_map()
        map.create_one_floor(29, 1)
        get_map = map.get_map()
        for i in get_map:
            print(i)
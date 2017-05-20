class NORTH:
    pass


class EAST:
    pass


class SOUTH:
    pass


class WEST:
    pass


class Robot(object):
    def __init__(self, facing=NORTH, pos_x=0, pos_y=0):
        self.coordinates = (pos_x, pos_y)
        self.bearing = facing

    def advance(self):
        pass

    def simulate(self, text):
        pass

    def turn_right(self):
        pass

    def turn_left(self):
        pass

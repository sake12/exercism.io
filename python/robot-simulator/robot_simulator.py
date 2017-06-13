NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


class Robot(object):
    def __init__(self, bearing=NORTH, pos_x=0, pos_y=0):
        self.coordinates = (pos_x, pos_y)
        self.bearing = bearing

    def advance(self):
        coords = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0),
        }

        add = coords[self.bearing]
        self.coordinates = (self.coordinates[0] + add[0],
                            self.coordinates[1] + add[1])

    def simulate(self, text):
        command = {
            'A': self.advance,
            'L': self.turn_left,
            'R': self.turn_right
        }

        for move in text:
            command[move]()

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

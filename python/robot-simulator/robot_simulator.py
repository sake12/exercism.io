NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


class Robot(object):
    def __init__(self, bearing=NORTH, pos_x=0, pos_y=0):
        self.coordinates = (pos_x, pos_y)
        self.bearing = bearing

    def advance(self):
        coords = self.coordinates
        if self.bearing == NORTH:
            self.coordinates = (coords[0], coords[1] + 1)
        elif self.bearing == EAST:
            self.coordinates = (coords[0] + 1, coords[1])
        elif self.bearing == SOUTH:
            self.coordinates = (coords[0], coords[1] - 1)
        elif self.bearing == WEST:
            self.coordinates = (coords[0] - 1, coords[1])

    def simulate(self, text):
        for move in text:
            if move == 'A':
                self.advance()
            elif move == 'L':
                self.turn_left()
            elif move == 'R':
                self.turn_right()

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4


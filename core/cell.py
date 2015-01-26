__author__ = 'Alexey'


class Cell:
    def __init__(self, x=0, y=0, state=0):
        self.x = x
        self.y = y
        self.state = state

    def get_coordinates(self):
        """
        Returns the cell's center coordinates.
        """
        return self.x, self.y

    def get_condition(self):
        """
        Return the state for the cell:\n
        0 for free cell,\n
        1 for the cell with o inside,\n
        2 for the cell with x inside.
        """
        return self.state

    def set_state(self, condition):
        """
        Setting condition for the cell:
        0 for free cell, 1 for the cell with o inside, 2 for the cell with x inside
        """
        self.state = condition

    def __str__(self):
        return 'x: %d; y: %d; state: %d' % (self.x, self.y, self.state)
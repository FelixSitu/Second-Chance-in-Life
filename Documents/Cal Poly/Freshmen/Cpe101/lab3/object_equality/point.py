from utility import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y)

    """def __ne__(self, other):
        return not self.__eq__(other)"""



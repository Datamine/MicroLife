#!/usr/bin/python3

class Vector(object):
    """
    represents a coordinate pair in the x,y plane
    """

    def __init__(self, x, y):
        """
        set the following instance variables:
            - x: float
            - y: float
        """

        self.x = x
        self.y = y

    def __add__(self, new_vector):
        """
        returns a new vector representing the linear addition of the two vectors.
        does not overwrite the coordinates of either argument vector.
        """
        return Vector(self.x + new_vector.x, self.y + new_vector.y)

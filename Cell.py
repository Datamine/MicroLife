#!/usr/bin/python3

import random
from Utilities.vector import Vector

class Cell(object):
    """
    represents a single cell in an organism.
    """

    def __init__(self, position, parent_organism, energy_stored, energy_required):
        """
        set the following instance variables:
            - position: Vector, position in the x/y plane
            - parent_organism: Organism, the parent organism of the cell
            - energy_stored: float, the amount of energy stored by the cell
            - energy_required: float, amount of energy the cell requires to live for a timestep
        """

        # position is passed in as a regular old tuple RN -- must fix
        self.position = Vector(position[0], position[1])
        self.parent_organism = parent_organism
        self.energy_stored = energy_stored
        self.energy_required = energy_required

    def available_adjacent_spaces(self):
        """
        returns list of empty spaces adjacent (not diagonally) to this cell
        """

        directions = [Vector(0,1), Vector(0,-1), Vector(1, 0), Vector(-1, 0)]
        potential_locs = [self.position + v for v in directions]
        return [(v.x, v.y) for v in potential_locs if self.parent_organism.parent_board.board[v.x][v.y] == None]

    def has_available_adjacent_space(self):
        """
        return True if there's at least one empty space (not diagonally) adjacent
        to this cell, False otherwise
        """

        return any(self.available_adjacent_spaces())

    def pick_available_adjacent_space(self):
        """
        returns a random empty space adjacent to this cell (not diagonally)
        """

        return random.choice(self.available_adjacent_spaces())



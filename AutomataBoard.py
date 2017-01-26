"""
John Loeber | contact@johnloeber.com | Dec 17 2016 | Python 2.7.12
"""

from random import random, randint, choice
import logging
logging.basicConfig(filename='fin.log',level=logging.DEBUG)

def log(string):
    #logging.info(string)
    print string
    return

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cell(object):
    """
    represents a single cell in an organism.
    """

    def __init__(self, x, y, parent_organism, energy_stored, energy_required):
        """
        set the following:
            - the parent organism of the cell (type: class Organism)
            - the amount of energy stored by the cell (type: float)
            - amount of energy the cell requires to live through a timestep
        """

        self.x = x
        self.y = y
        self.parent_organism = parent_organism
        self.energy_stored = energy_stored
        self.energy_required = energy_required

class Organism(object):
    """
    represents an organism: a contiguous amalgam of cells
    """

    def __init__(self, x, y, p_cell_death, parent_board, food):
        """
        where x_bound and y_bound denote the dimensions of the board;
        initialize the organism with:
            - a cell
            - a utility function
            - a consumption function
            - a reproduction function
        """

        self.cells = []
        self.parent_board = parent_board
        self.p_cell_death = p_cell_death
        self.food = food

        # spawn the initial cell
        self.spawn_cell(x, y)
        return

    def spawn_cell(self, x, y):
        self.cells.append(Cell(x, y, self))
        return

    def timestep(self, movement):
        """
        movement (type: class Vector)
        the movement is a standard unit vector, i.e. (0,1), (1,0), (0,-1), (-1,0)
        """

        # handle cell deaths
        live_cells = []

        for cell in self.cells:
            if random() > self.p_cell_death:
                live_cells.append(cell)

        # handle cell movement
        live_cell_energy = get_energy(live_cells)

        moved_cells = []

        for cell in live_cells:
            if self.isMovable(cell)


        return

    def isMovable(self, cell, movement):
        new_x = cell.x + movement.x
        new_y = cell.y + movement.y

        if 0 <= new_x < self.parent_board.size_x and 0 <= new_y < self.parent_board.size_y:
            # gotta figure out how to consume food, objects, etc.
        return False

class Board(object):
    """
    represents a board consisting of squares: may contain organisms and food
    (TODO: what if all organisms are food? create a predator structure.)
    """
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = [[None] * self.size_x for _ in range(self.size_y)]
        self.organisms = []
        self.resources = []

    def get_random_empty_square(self):
        """
        return a random empty square.
        this algorithm is highly inefficient, but it works given
        the computing power of my laptop. maybe i'll design a more efficient
        datastructure + algorithm to make this function more scalable.
        """
        empty_indices = []
        for i in range(self.size_y):
            for j in range(self.size_x):
                if self.board[i][j] != None:
                    empty_indices.append((i, j))

        return choice(empty_indices)

    def spawn_organisms(self, number):
        """
        number: amount of such organisms to add
        """
        for _ in xrange(number):
            x, y = self.get_random_empty_square()
            # want to randomly configure these components
            p_cell_death = 0.2
            organisms.append(Organism(x, y, p_cell_death, self))
        return

    #def add_resource(self, resource):
    #    append_item_or_list_to_list(resource, self.resources)
    #    return

#        append_item_or_list_to_list(resource, self.organisms)

def get_energy(cells):
    """
    get the total energy stored in a list of cells
    """
    return sum(cell.energy_stored for cell in cells)


def append_item_or_list_to_list(to_append, _list):
    if type(to_append) == list:
        _list += to_append
    else:
        _list.append(to_append)

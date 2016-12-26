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

class Cell(object):
    """
    represents a single cell in an organism.
    """

    def __init__(self, x, y, probability):
        """
        initialize the cell, set the probability of death on a timestep
        """
        self.x = x
        self.y = y
        self.pdeath = probability
        #self.energy_stored = energy_stored
        #self.energy_required =

    def timestep(self, x_move, y_move):
        """
        update the cell's movement on a timestep, check for death
        """
        self.x += x_move
        self.y += y_move
        if random.random() < self.pdeath:
            return "Dead"
        else:
            return "Alive"

class Organism(object):
    """
    represents an organism: a contiguous amalgam of cells
    """

    def __init__(self, x, y, p_cell_death, parent_board):
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


        spawn_initial_cell(x_bound, y_bound)

    def spawn_initial_cell(self):

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
                    empty_indices.append((i,j))

        return choice(empty_indices)

    def spawn_organisms(self, number):
        """
        number: amount of such organisms to add
        """
        for i in xrange(number):
            x, y = self.get_random_empty_square()
            # want to randomly configure these components
            p_cell_death = 0.2
            organisms.append(Organism(x, y, p_cell_death, self))
        return

    #def add_resource(self, resource):
    #    append_item_or_list_to_list(resource, self.resources)
    #    return

#        append_item_or_list_to_list(resource, self.organisms)
def append_item_or_list_to_list(to_append, _list):
    if type(to_append) == list:
        _list += to_append
    else:
        _list.append(to_append)

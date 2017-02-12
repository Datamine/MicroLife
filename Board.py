#!/usr/bin/python3
"""
John Loeber | contact@johnloeber.com | Dec 17 2016 | Python 3.6.0
"""

from Organism import Organism
from ImageColor import getrgb
import pygame

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
        self.timestep = 0
        self.visualize = False
        self.screen = None

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

    def visualize(self):
        """
        runs pygame to visualize the evolution of the board.
        """
        self.visualize = True
        pygame.init()
        size = (self.size_x, self.size_y + 100)
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(Colors.white)

    def timestep(self):
        """
        runs the timestep logic for all constituent organisms,
        """
        self.timestep += 1

    #def add_resource(self, resource):
    #    append_item_or_list_to_list(resource, self.resources)
    #    return

#        append_item_or_list_to_list(resource, self.organisms)



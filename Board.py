#!/usr/bin/python3
"""
John Loeber | contact@johnloeber.com | Dec 17 2016 | Python 3.6.0
"""

from Organism import Organism
from random import choice
import Colors
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
        self.timestep_number = 0
        self.visualization = False
        self.screen = None

        self.spawn_organisms(1)

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
                if self.board[i][j] is None:
                    empty_indices.append((i, j))

        return choice(empty_indices)

    def spawn_organisms(self, number):
        """
        number: amount of such organisms to add
        """
        for _ in range(number):
            # want to randomly configure these components
            self.organisms.append(Organism(self))
        return

    def visualize(self):
        """
        runs pygame to visualize the evolution of the board.
        """
        self.visualization = True
        pygame.init()
        pygame.display.set_caption("MicroLife")
        size = (self.size_x, self.size_y + 50)
        self.screen = pygame.display.set_mode(size)

    def timestep(self):
        """
        runs the timestep logic for all constituent organisms,
        refreshes the visualization
        """
        self.timestep_number += 1
        self.screen.fill(Colors.white)

        # handle timesteps for all constituent organisms
        self.board = [[None] * self.size_x for _ in range(self.size_y)]
        for organism in self.organisms:
            organism.timestep()

        # render the current timestamp as text
        instruct = pygame.font.Font('Fonts/BebasNeue.ttf',26)
        timestep_count = instruct.render("Timestep: " + str(self.timestep_number), 1, Colors.black)
        # the second argument to blit is the coordinate
        self.screen.blit(timestep_count, (10, self.size_y + 10))
        # render a line to separate the timestamp from the main simulation area
        pygame.draw.line(self.screen, Colors.black, (0, self.size_y), (self.size_x, self.size_y))

        # render everything on the board
        for row_index, row in enumerate(self.board):
            for cell_index, cell in enumerate(row):
                if not cell is None:
                    # will eventually add color-codes for different organisms, food, etc.
                    # use blit if I decide to go for larger blocks
                    self.screen.set_at((row_index, cell_index), Colors.black)

        pygame.display.flip()

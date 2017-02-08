#!/usr/bin/python3
"""
John Loeber | contact@johnloeber.com | Dec 17 2016 | Python 3.6.0
"""

import random
from Cell import Cell

class Organism(object):
    """
    represents an organism: a contiguous amalgam of cells
    """

    def __init__(self, parent_board, p_cell_death):
        """
        set the following instance variables:
            - parent_board: Board, the board that contains this organism
            - p_cell_death: float, the probability for a given cell to die on a timestep
            - cells: list of Cell, the cells that the organism contains
        """

        self.parent_board = parent_board
        self.p_cell_death = p_cell_death
        self.cells = []

        # spawn the initial cell
        self.spawn_cell()

    def total_energy(self):
        """
        returns the total energy stored in all the organism's constituent cells
        """

        return sum(c.energy_stored for c in self.cells)

    def spawn_cell(self):
        """
        creates a new cell and appends it to the array of existing cells for this organism.
        if some cells already exist, then it creates a new cell at an adjacent
        square. Only works if such a square is available.
        """
        new_posn = None
        if self.cells:
            available_cells = [c for c in self.cells if c.has_available_adjacent_space()]
            if available:
                new_posn = random.choice(available_cells).pick_available_space()
        else:
            new_posn = parent_board.get_empty_square()

        if not new_posn is None:
            new_cell = Cell(position=new_posn, parent_organism=self,
                            energy_stored=100, energy_required=1)
            self.cells.append(new_cell)

    def cell_deaths(self):
        """
        handle cell deaths
        """

        live_cells = []
        for cell in self.cells:
            if random.random() > self.p_cell_death:
                live_cells.append(cell)
        self.cells = live_cells

    def timestep(self):
        """
        handle the events that happen between timesteps:
        cell death and org movement
        """

        self.cell_deaths()

    """
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
    """

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



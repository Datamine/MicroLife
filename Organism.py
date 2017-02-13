#!/usr/bin/python3

import random
from Cell import Cell

class Organism(object):
    """
    represents an organism: a contiguous amalgam of cells
    """

    def __init__(self, parent_board):
        """
        set the following instance variables:
            - parent_board: Board, the board that contains this organism
            # - p_cell_death: float, the probability for a given cell to die on a timestep
            - cells: list of Cell, the cells that the organism contains
        """

        self.parent_board = parent_board
        # would like to set p_cell_death from a config file
        self.p_cell_death = 0.01
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
            if available_cells:
                new_posn = random.choice(available_cells).pick_available_adjacent_space()
        else:
            new_posn = self.parent_board.get_random_empty_square()

        if not new_posn is None:
            new_cell = Cell(position=new_posn, parent_organism=self,
                            energy_stored=1000, energy_required=1)
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
        for _ in range(10):
            self.spawn_cell()

        for cell in self.cells:
            self.parent_board.board[cell.position.x][cell.position.y] = cell

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



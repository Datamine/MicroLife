#!/usr/bin/python3
"""
John Loeber | contact@johnloeber.com | Dec 17 2016 | Python 3.6.0
"""

from Board import Board
from time import sleep

def get_energy(cells):
    """
    get the total energy stored in a list of cells
    """
    return sum(cell.energy_stored for cell in cells)

def main():
    """
    instantiates a new board, as well as a visualization
    """
    board = Board(512, 512)
    board.visualize()
    for i in range(1000):
        board.timestep()
        sleep(0.01)
    while True:
        pass

if __name__ == '__main__':
    main()

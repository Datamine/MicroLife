#!/usr/bin/python3
"""
John Loeber | contact@johnloeber.com | Dec 17 2016 | Python 3.6.0
"""

from Board import Board

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

if __name___ == '__main__':
    main()

__author__ = 'Alexey'
from cell import *
import random
from colors import *
import sys


def get_square_center(x, y):
    left_up_corner = (x - x % 40, y - y % 40)
    result = (left_up_corner[0] + 20, left_up_corner[1] + 20)
    return result


def init_table():
    table = {}
    for i in range(20, 400, 40):
        for j in range(20, 400, 40):
            table[(i, j)] = Cell(i, j)
    return table


def get_free_cells(all_cells):
    result = []
    for cell in all_cells:
        if cell.state == 0:
            result.append(cell)
    return result


def get_player_cells(all_cells):
    result = {}
    for cell in all_cells:
        if cell.state == 1:
            result[cell.get_coordinates()] = cell
    return result


def get_computer_cells(all_cells):
    result = {}
    for cell in all_cells:
        if cell.state == 2:
            result[cell.get_coordinates()] = cell
    return result


def contains(list, element):
    try:
        list.index(element)
    except ValueError:
        return False
    return True


def check_cells_sequence(cell, cells_container, x_direction, y_direction):
    x = cell.get_coordinates()[0]
    y = cell.get_coordinates()[1]
    for i in range(1, 5, 1):
        try:
            cells_container[(x + x_direction * i * 40, y + y_direction * i * 40)]
        except KeyError:
            return False
    return True


def check_for_win(table):
    player_cells = get_player_cells(table.values())
    computer_cells = get_computer_cells(table.values())

    for cell in player_cells.values():
        if check_cells_sequence(cell, player_cells, -1, -1) or \
                check_cells_sequence(cell, player_cells, 0, -1) or \
                check_cells_sequence(cell, player_cells, 1, -1) or \
                check_cells_sequence(cell, player_cells, 1, 0) or \
                check_cells_sequence(cell, player_cells, 1, 1) or \
                check_cells_sequence(cell, player_cells, 0, 1) or \
                check_cells_sequence(cell, player_cells, -1, 1) or \
                check_cells_sequence(cell, player_cells, -1, 0):
            print "Player win!"
            return 1
    for cell in computer_cells.values():
        if check_cells_sequence(cell, computer_cells, -1, -1) or \
                check_cells_sequence(cell, computer_cells, 0, -1) or \
                check_cells_sequence(cell, computer_cells, 1, -1) or \
                check_cells_sequence(cell, computer_cells, 1, 0) or \
                check_cells_sequence(cell, computer_cells, 1, 1) or \
                check_cells_sequence(cell, computer_cells, 0, 1) or \
                check_cells_sequence(cell, computer_cells, -1, 1) or \
                check_cells_sequence(cell, computer_cells, -1, 0):
            print "Computer win!"
            return 2
    return 0


def end_game(pygame):
    pygame.quit()
    sys.exit()



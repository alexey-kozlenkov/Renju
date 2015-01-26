__author__ = 'Alexey'
from cell import *
import random
from colors import *


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


def get_free_cells(cells):
    result = []
    for cell in cells:
        if cell.state == 0:
            result.append(cell)
    return result


def get_player_cells(cells):
    result = {}
    for cell in cells:
        if cell.state == 1:
            result[cell.get_coordinates()] = cell
    return result


def get_computer_cells(cells):
    result = {}
    for cell in cells:
        if cell.state == 2:
            result[cell.get_coordinates()] = cell
    return result


def computer_turn(pygame, DISPLAYSURFACE, table):
    free_cells = get_free_cells(table.values())
    position = random.randint(0, len(free_cells) - 1)
    free_cells[position].set_state(2)
    draw_cross(pygame, DISPLAYSURFACE, free_cells[position])


def draw_cross(pygame, DISPLAYSURFACE, computer_point):
    pygame.draw.line(DISPLAYSURFACE, RED,
                     (computer_point.get_coordinates()[0] - 10, computer_point.get_coordinates()[1] - 10),
                     (computer_point.get_coordinates()[0] + 10, computer_point.get_coordinates()[1] + 10), 3)
    pygame.draw.line(DISPLAYSURFACE, RED,
                     (computer_point.get_coordinates()[0] - 10, computer_point.get_coordinates()[1] + 10),
                     (computer_point.get_coordinates()[0] + 10, computer_point.get_coordinates()[1] - 10), 3)


def check_for_free(free_cells, cell):
    try:
        free_cells.index(cell)
    except ValueError:
        return False
    return True


def check_cells_sequence(cell, cells, x_direction, y_direction):
    x = cell.get_coordinates()[0]
    y = cell.get_coordinates()[1]
    for i in range(1, 5, 1):
        try:
            cells[(x + x_direction * i * 40, y + y_direction * i * 40)]
        except KeyError:
            return False
    return True


def check_for_winner(table):
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
            return 2
    return 0



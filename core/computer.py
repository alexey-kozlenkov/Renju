__author__ = 'Alexey'
from functions import *


def computer_turn(pygame, DISPLAYSURFACE, table):
    free_cells = get_free_cells(table.values())
    position = random.randint(0, len(free_cells) - 1)
    free_cells[position].set_state(2)
    draw_cross(pygame, DISPLAYSURFACE, free_cells[position])


def get_position_for_shoot(table):
    free_cells = get_free_cells(table.values)
    for cell in free_cells:
        pass


def draw_cross(pygame, DISPLAYSURFACE, computer_point):
    pygame.draw.line(DISPLAYSURFACE, RED,
                     (computer_point.get_coordinates()[0] - 10, computer_point.get_coordinates()[1] - 10),
                     (computer_point.get_coordinates()[0] + 10, computer_point.get_coordinates()[1] + 10), 3)
    pygame.draw.line(DISPLAYSURFACE, RED,
                     (computer_point.get_coordinates()[0] - 10, computer_point.get_coordinates()[1] + 10),
                     (computer_point.get_coordinates()[0] + 10, computer_point.get_coordinates()[1] - 10), 3)

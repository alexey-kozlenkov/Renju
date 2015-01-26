__author__ = 'Alexey'
import sys

import pygame
from pygame.locals import *

from functions import *

pygame.init()
DISPLAYSURFACE = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Renju v1.0')
table = init_table()

DISPLAYSURFACE.fill(WHITE)
for i in range(40, 361, 40):
    pygame.draw.line(DISPLAYSURFACE, BLACK, (0, i), (400, i))
    pygame.draw.line(DISPLAYSURFACE, BLACK, (i, 0), (i, 400))

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mpos = get_square_center(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            cell = table.get(mpos)
            free_cells = get_free_cells(table.values())
            if not check_for_free(free_cells, cell):
                break

            cell.set_state(1)
            pygame.draw.circle(DISPLAYSURFACE, BLUE, mpos, 15, 3)
            pygame.display.update()

            computer_turn(pygame, DISPLAYSURFACE, table)
            pygame.display.update()

            winner_check = check_for_winner(table)
            if winner_check == 1:
                print "Player win!"
                pygame.quit()
                sys.exit()
            elif winner_check == 2:
                print "Computer win!"
                pygame.quit()
                sys.exit()
    pygame.display.update()



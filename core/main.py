__author__ = 'Alexey'
import sys
import pygame
from pygame.locals import *
from colors import *
from functions import *


pygame.init()
DISPLAYSURFACE = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello World!')

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
            mpos = pygame.mouse.get_pos()
            pygame.display.set_caption(str(mpos))
            pygame.draw.circle(DISPLAYSURFACE, BLUE, get_square_center(mpos[0], mpos[1]), 15, 2)
    pygame.display.update()
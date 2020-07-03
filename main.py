import pygame
from board import Board
# Init here
pygame.init()
# Variables here

width = 500
height = 500
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
board = Board()
input(board.tiles)

# Window of the game here
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board.draw_tiles(window)
    # pygame.draw.rect(window,(255,0,0),[0,0,400,400])
    pygame.display.update()

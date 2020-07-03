import pygame
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


# Window of the game here
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tile_color = WHITE
    line = 0
    for i in range(0,8):
        line+=1
        if line % 2 == 1:
            tile_color = WHITE
        else:
            tile_color = BLACK

        for j in range(0,8):
            pygame.draw.rect(window,tile_color,[j*50,i*50,50,50])
            if tile_color == WHITE:
                tile_color = BLACK
            else:
                tile_color = WHITE
    # pygame.draw.rect(window,(255,0,0),[0,0,400,400])
    pygame.display.update()
    
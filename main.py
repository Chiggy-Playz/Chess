import pygame
# Init here
pygame.init()
# Variables here
width = 800
height = 600
# Window of the game here
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

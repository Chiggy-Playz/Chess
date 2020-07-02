import pygame
# Init here
pygame.init()
# Variables here
width = 800
height = 600
white = (255,255,255)
black = (0,0,0)
# Window of the game here
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('chess')
running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True 
    window.fill(white)
    pygame.draw.rect(window,black,['400','300','10','100'])
    pygame.display.update()
pygame.quit()

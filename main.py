import pygame
# Init here
pygame.init()
# Variables here
# Width and height of the game
width = 800
height = 600
# Colors here (Red,Green,Blue)
white = (255,255,255)
black = (0,0,0)
# This will make the images load
Pawn = pygame.image.load('white-pawn-md.png')
PawnX = 400
pawnY = 200
def Pawn():
    pygame.blip(Pawn,PawnX,pawnY)
# End of variables and function defining
# Window of the game here
window = pygame.display.set_mode((width,height))
# Name of the game here
pygame.display.set_caption('chess')
# Main loop here
running = True
# This will make it to for the user to close out of the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# This is to make the screen white
    window.fill(white)
    pygame.draw.rect(window,black,[500,100,20,100])
    Pawn()
    pygame.display.update()
# You also need this to quit for me
pygame.quit()

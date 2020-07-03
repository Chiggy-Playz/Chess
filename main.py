import pygame
from board import Board
# Init here
pygame.init()
# Variables here


width = 800
height = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
board = Board()
x =  (width * 0.45)
y = (height * 0.8)
# Here is every piece
Whitepawnimg = pygame.image.load('whitepawn.png')
Whitekingimg = pygame.image.load('whiteking.png')
Whitequeenimg = pygame.image.load('whitequeen.png')
Whitebishopimg = pygame.image.load('whitebishop.png')
Whiterookimg = pygame.image.load('whiterook.png')
Whiteknightimg = pygame.image.load('whiteknight') 
blackpawnimg = pygame.image.load('blackpawn.png')
blackkingimg = pygame.image.load('blackking.png')
blackqueenimg = pygame.image.load('blackqueen.png')
blackbishopimg = pygame.image.load('blackbishop.png')
blackrookimg = pygame.image.load('blackrook.png')
blackknightimg = pygame.image.load('blackknight.png') 
# Now for the board
boardimg = pygame.image.load('board.png')
# Window of the game here
window = pygame.display.set_mode((width,height))
# Name of the game here
pygame.display.set_caption('Chess')
# Main loop here
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board.draw_tiles(window)
    
    img_rect = img.get_rect()
    window.blit(img,(0,0))
    # pygame.draw.rect(window,(255,0,0),[0,0,400,400])
    pygame.display.update()

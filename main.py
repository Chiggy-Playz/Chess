import pygame
# Init here
pygame.init()
# Variables here
# In computers there are only 255 called RGB here it is red green blue 
width = 1000
height = 800
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
# Sise of the game here
window = pygame.display.set_mode((width,height))
# Name of the game here
pygame.display.set_caption('Chess')
# Putting all images here
# This will load the image here
Whitepawnimg = pygame.image.load('whitepawn.png')
def whitepawn(whitepawnx,whitepawny):
    window.blit(Whitepawnimg,(whitepawnx,whitepawny))
whitepawnx = (width*0.2)
whitepawny = (height*0,4)


Whitebishopimg = pygame.image.load('whitebishop.png')
def whitebishop(whitebishopx,whitebishopy):
    window.blit(Whitebishopimg,(whitebishopx,whitebishopy))
whitebishopx= (width*0.2)
whitebishopy= (height*0,4)
Whiteknightimg = pygame.image.load('whiteknight.png')
def whiteknight(whiteknightx,whiteknighty):
        window.blit(Whiteknightimg,(whiteknightx,whiteknighty))
whiteknightx= (width*0.2)
whiteknighty= (height*0,4)
Whiterookimg = pygame.image.load('whiterook.png')
def whiterook(whiterookx,whiterooky):
        window.blit(Whiterookimg,(whiterookx,whiterooky))
whiterookx = (width*0.2)
whiterooky = (height*0,4)
Whitequeenimg = pygame.image.load('whitequeen.png')
def whitequeen(whitequeenx,whitequeeny):
        window.blit(Whitequeenimg,(whitequeenx,whitequeeny))
whitequeenx = (width*0.2)
whitequeeny = (height*0,4)
Whitekingimg = pygame.image.load('whiteking.png')
def whiteking(whitekingx,whitekingy):
        window.blit(Whitekingimg,(whitekingx,whitekingx))
whitekingx = (width*0.2)
whitekingy = (height*0,4)
blackpawnimg = pygame.image.load('blackpawn.png')
def blackpawn(blackpawnx,blackpawny):
        window.blit(blackpawnimg,(blackpawnx,blackpawny))
blackpawnx= (width*0.2)
blackpawny = (height*0,4)
blackbishopimg = pygame.image.load('blackbishop.png')
def blackbishop(blackbishopx,blackbishopy):
        window.blit(blackbishopimg,(blackbishopx,blackbishopy))
blackpawnx= (width*0.2)
blackpawny = (height*0,4)
blackknightimg = pygame.image.load('blackknight.png')
def blackknight(blackknightx,blackknighty):
        window.blit(blackknightimg,(blackknightx,blackknighty))
blackpawnx= (width*0.2)
blackpawny = (height*0,4)

blackrookimg = pygame.image.load('blackrook.png')
def blackrook(blackrookx,blackrooky):
        window.blit(blackrookimg,(blackrookx,blackrooky))
blackrookx = (width*0.2)
blackrookx = (height*0,4)
blackqueenimg = pygame.image.load('blackqueen.png')
def blackqueen(blackqueenx,blackqueeny):
        window.blit(blackqueenimg,(blackqueenx,blackqueeny))
blackqueenx = (width*0.2)
blackqueeny = (height*0,4)
blackkingimg = pygame.image.load('blackking.png')
def blackking(blackkingx,blackkingy):
        window.blit(blackkingimg,(blackkingx,blackkingy))
blackkingx = (width*0.8)
blackkingy = (height*0.4)
# Now for the board
boardimg = pygame.image.load('board.png')
def board(boardx,boardy):
    window.blit(boardimg,(boardx,boardy))
boardx = (width * 0,2)
boardy = (height * 0,4)
boardimg = pygame.transform.scale(boardimg,(1000,800))
# Main loop here
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board(boardx,boardy)
    pygame.display.update()
pygame.quit()
quit()

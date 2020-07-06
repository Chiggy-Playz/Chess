import pygame
# Init here
pygame.init()
# Variables here
# Width and height of the window 
width_window = 800
height_window = 600
# Width and height of the pawns
width_whitepawn = 80
height_whitepawn = 40
width_whitebishop = 50
height_whitebishop = 50
width_whiteknight = 50
height_whiteknight = 50
width_whiterook = 50
height_whiterook = 50
width_whitequeen = 50
height_whitequeen = 50
width_whiteking = 50
height_whiteking = 50
# Now for the black pawns
width_blackpawn = 60
height_blackpawn = 50
width_blackbishop = 50
height_blackbishop = 50
width_blackknight = 50
height_blackknight = 50
width_blackrook = 50
height_blackrook = 50
width_blackqueen = 50
height_blackqueen = 50
width_blackking = 50
height_blackking = 50
# Now for the images
# This will load the images here
whitepawnimg = pygame.image.load('whitepawn.png')
Whitebishopimg = pygame.image.load('whitebishop.png')
Whiteknightimg = pygame.image.load('whiteknight.png')
Whiterookimg = pygame.image.load('whiterook.png')
Whitequeenimg = pygame.image.load('whitequeen.png')
Whitekingimg = pygame.image.load('whiteking.png')
# Now for the black pieces
blackpawnimg = pygame.image.load('blackpawn.png')
blackbishopimg = pygame.image.load('blackbishop.png')
blackknightimg = pygame.image.load('blackknight.png')
blackrookimg = pygame.image.load('blackrook.png')
blackqueenimg = pygame.image.load('blackqueen.png')
blackkingimg = pygame.image.load('blackking.png')
# Now for the board
boardimg = pygame.image.load('board.png')
# Size of the game here
window = pygame.display.set_mode((width_window,height_window))
# Name of the game here
pygame.display.set_caption('Chess')
# Here will have x and y of the pawns
# You might have a question what is the difference uptop and here
# Uptop is the size of the image here is where it's place in the window i hope that sorts the confusion

whitepawnx = (width_window*0.4)
whitepawny = (height_window*0.78)
whitebishopx = (width_window*0.2)
whitebishopy = (height_window*0.4)
whiteknightx = (width_window*0.2)
whiteknighty = (height_window*0.4)
whiterookx = (width_window*0.2)
whiterooky = (height_window*0.4)
whiterookx = (width_window*0.2)
whiterooky = (height_window*0.4)
whitequeenx = (width_window*0.2)
whitequeeny = (height_window*0.4)
whitekingx = (width_window*0.2)
whitekingy = (height_window*0.4)
# Now for the black pawns
blackpawnx= (width_window*0.2)
blackpawny = (height_window*0.4)
blackbishopx= (width_window*0.2)
blackbishopy = (height_window*0.4)
blackknightx = (width_window*0,4)
blackknighty = (height_window*0,2)
blackrookx = (width_window*0.2)
blackrookx = (height_window*0.4)
blackqueenx = (width_window*0.2)
blackqueeny = (height_window*0.4)
blackkingx = (width_window*0.8)
blackkingy = (height_window*0.4)
# Now for the board
boardx = (width_window * 0.0)
boardy = (height_window * 0.0)
# Now we need to use the function or the method to manipulate the placement
whitepawnimg = pygame.transform.scale(whitepawnimg,(width_whitepawn,height_whitepawn))
whitebishopimg = pygame.transform.scale(whitebishopimg,(width_whitebishop,height_whitebishop))
whiteknightimg = pygame.transform.scale(whiteknightimg,(width_whiteknight,height_knight))
whiterookimg = pygame.transform.scale(whiterookimg,(width_whiterook,height_whiterook))
whitequeenimg = pygame.transform.scale(whitequeenimg,(width_whitequeen,height_whiterook))
whitekingimg = pygame.transform.scale(whitekingimg,(width_blackking,height_whiteking))
# Now for the black pawns
blackpawnimg = pygame.transform.scale(blackpawnimg,(width_blackpawn,height_blackpawn))
blackbishopimg = pygame.transform.scale(blackbishopimg,(width_whitebishop,height_blackbishop))
blackknightimg = pygame.transform.scale(blackknightimg,(width_blackknight,height_blackknight))
blackrookimg = pygame.transform.scale(blackrookimg,(width_blackrook,height_blackrook))
blackqueenimg = pygame.transform.scale(blackqueenimg,(width_blackqueen,height_blackrook))
blackkingimg = pygame.transform.scale(blackking,(width_blackking,height_blackking))
# Now for the board
boardimg = pygame.transform.scale(boardimg,(width_window,height_window))
# Now for function of blit to show it to the screen
def whitepawn(whitepawnx,whitepawny):
    window.blit(whitepawnimg,(whitepawnx,whitepawny))

def whitebishop(whitebishopx,whitebishopy):
    window.blit(Whitebishopimg,(whitebishopx,whitebishopy))

def whiteknight(whiteknightx,whiteknighty):
    window.blit(Whiteknightimg,(whiteknightx,whiteknighty))

def whiterook(whiterookx,whiterooky):
    window.blit(Whiterookimg,(whiterookx,whiterooky))

def whitequeen(whitequeenx,whitequeeny):
    window.blit(Whitequeenimg,(whitequeenx,whitequeeny))

def whiteking(whitekingx,whitekingy):
    window.blit(Whitekingimg,(whitekingx,whitekingx))

def blackpawn(blackpawnx,blackpawny):
    window.blit(blackpawnimg,(blackpawnx,blackpawny))


def blackbishop(blackbishopx,blackbishopy):
    window.blit(blackbishopimg,(blackbishopx,blackbishopy))

def blackknight(blackknightx,blackknighty):
    window.blit(blackknightimg,(blackknightx,blackknighty))

def blackrook(blackrookx,blackrooky):
    window.blit(blackrookimg,(blackrookx,blackrooky))
def blackqueen(blackqueenx,blackqueeny):
    window.blit(blackqueenimg,(blackqueenx,blackqueeny))

def blackking(blackkingx,blackkingy):
    window.blit(blackkingimg,(blackkingx,blackkingy))

def board(boardx,boardy):
    window.blit(boardimg,(boardx,boardy))

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

import pygame
# Init here
pygame.init()
# Variables here
# Width and height of the window 
width_window = 800
height_window = 600
# Width and height of the pieces
width_pieces = 80
height_pieces = 40
# Now for the images
# This will load the images here

whitepawnimg = pygame.image.load('whitepawn.png')
whitebishopimg = pygame.image.load('whitebishop.png')
whiteknightimg = pygame.image.load('whiteknight.png')
whiterookimg = pygame.image.load('whiterook.png')
whitequeenimg = pygame.image.load('whitequeen.png')
whitekingimg = pygame.image.load('whiteking.png')
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
whitepawnx1 = (width_window*0.4)
whitepawny1 = (height_window*0.78)

whitepawnx2 = (width_window*0,3)
whitepawny2 = (height_window*0,8)

whitepawnx3 = (width_window*0,2)
whitepawny3 = (height_window*0,4)
whitepawnx4 = (width_window*0,2)
whitepawny4 = (height_window*0,5)

whitepawnx5 = (width_window*0,2)
whitepawny5 = (height_window*0,4)

whitepawnx6 = (width_window*0,5)
whitepawny6 = (height_window*0,2)

whitepawny7 = (width_window*0,2)
whitepawnx7 = (height_window*0,2)

whitepawny8 =(width_window*0,4)
whitepawnx8 = (height_window*0,2)
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
# Now for the black peices
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
whitepawnimg = pygame.transform.scale(whitepawnimg,(width_pieces,height_pieces))
whitebishopimg = pygame.transform.scale(whitebishopimg,(width_pieces,height_pieces))
whiteknightimg = pygame.transform.scale(whiteknightimg,(width_pieces,height_pieces))
whiterookimg = pygame.transform.scale(whiterookimg,(width_pieces,height_pieces))
whitequeenimg = pygame.transform.scale(whitequeenimg,(width_pieces,height_pieces))
whitekingimg = pygame.transform.scale(whitekingimg,(width_pieces,height_pieces))
# Now for the black pawns
blackpawnimg = pygame.transform.scale(blackpawnimg,(width_pieces,height_pieces))
blackbishopimg = pygame.transform.scale(blackbishopimg,(width_pieces,height_pieces))
blackknightimg = pygame.transform.scale(blackknightimg,(width_pieces,height_pieces))
blackrookimg = pygame.transform.scale(blackrookimg,(width_pieces,height_pieces))
blackqueenimg = pygame.transform.scale(blackqueenimg,(width_pieces,height_pieces))
blackkingimg = pygame.transform.scale(blackkingimg,(width_pieces,height_pieces))
# Now for the board
boardimg = pygame.transform.scale(boardimg,(width_window,height_window))
# Now for function of blit to show it to the screen

def whitepawn(whitepawnx1,whitepawny1,whitepawnx2,whitepawny2,whitepawnx3,whitepawny3,whitepawnx4,
    whitepawny4,whitepawnx5,whitepawny5,whitepawnx6,whitepawny6,whitepawnx7,whitepawny7,whitepawnx8,
    whitepawny8):
    window.blit(whitepawnimg,(whitepawnx1,whitepawny1))
    window.blit(whitepawnimg,(whitepawnx2,whitepawny2))
    window.blit(whitepawnimg,(whitepawnx3,whitepawny3))
    window.blit(whitepawnimg,(whitepawnx4,whitepawny4))
    window.blit(whitepawnimg,(whitepawnx5,whitepawny5))
    window.blit(whitepawnimg,(whitepawnx6,whitepawny6))
    window.blit(whitepawnimg,(whitepawnx7,whitepawny7))
    window.blit(whitepawnimg,(whitepawnx8,whitepawny8))

    

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
    whitepawn(whitepawnx1,whitepawny1,whitepawnx2,whitepawny2,whitepawnx3,whitepawny3,whitepawnx4,
    whitepawny4,whitepawnx5,whitepawny5,whitepawnx6,whitepawny6,whitepawnx7,whitepawny7,whitepawnx8,
    whitepawny8)

    pygame.display.update()
pygame.quit()
quit()

import pygame

class Board:
    tiles = []
    def __init__(self):
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        tile_color = WHITE
        line = 0
        for i in range(0,8):
            line+=1
            if line % 2 == 1:
                tile_color = WHITE
            else:
                tile_color = BLACK
            for j in range(0,8):
                tile = {
                        "color":tile_color,
                        "posX":j*50,
                        "posY":i*50,
                        "width":50,
                        "height":50,
                        "chessPiece":None
                       }

                self.tiles.append(tile)
                if tile_color == WHITE:
                    tile_color = BLACK
                else:
                    tile_color = WHITE
    
    def draw_tiles(self,window):        
        for tile in self.tiles:
            rect = [tile["posX"], tile["posY"], tile["width"], tile["height"]]
            pygame.draw.rect(window,tile["color"],rect)
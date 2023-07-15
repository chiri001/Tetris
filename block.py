#helps define a block
from color import Color
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.color = Color.get_cell_colors()

    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 1, 
                                        tile.row * self.cell_size + 1, 
                                        self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)

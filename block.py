#helps define a block
from color import Color
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.color = Color.get_cell_colors()

    
    def move(self, row, col):
        self.row_offset += row
        self.col_offset += col

    def get_cell_pos(self): #position of occupied cell with offset applied
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, 
                                position.col + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if(self.rotation_state == -1):
            self.rotation_state = len(self.cells) - 1

    
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_pos()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.col * self.cell_size, 
                                        offset_y + tile.row * self.cell_size, 
                                        self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)

    

#to define structure of a grid
import pygame
from color import Color
class Grid:
    #intializes size of the grid
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i  in range(self.num_rows)]
        self.color = Color.get_cell_colors()
    
    #define print of the grid
    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end = " ")
            print()

    def in_bound(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                # to make grid visible add 1 offset at x and y  and remove 1 
                # pix from w and h makes it 29pix
                cell_rect = pygame.Rect(col * self.cell_size + 1, 
                                        row * self.cell_size + 1, 
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.color[cell_value], cell_rect)
    
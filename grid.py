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
    
    def is_row_full(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    
    def move_row_down(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0 #clear original row
    
    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def clear_full_row(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                # to make grid visible add 1 offset at x and y  and remove 1 
                # pix from w and h makes it 29pix
                cell_rect = pygame.Rect(col * self.cell_size + 11, 
                                        row * self.cell_size + 11, 
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.color[cell_value], cell_rect)
    
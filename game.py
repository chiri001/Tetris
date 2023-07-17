
from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), 
                       TBlock(), ZBlock() ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.clear_sound = pygame.mixer.Sound("sound/clear.mp3")
        self.game_over_sound = pygame.mixer.Sound("sound/gameover.mp3")
        self.game_over_sound_played = False


        pygame.mixer.music.load("sound/theme2.mp3")
        pygame.mixer.music.play(-1)#play music indefinately
    
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        if lines_cleared == 2:
            self.score += 300
        if lines_cleared == 3:
            self.score += 500
        if lines_cleared == 4:
            self.score += 650
        if lines_cleared >= 5 and lines_cleared <= 10:
            self.score += 1000
        if lines_cleared > 10:
            self.score += 5000
        self.score += move_down_points
        
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), 
                           TBlock(), ZBlock() ]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
        
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_in_bound() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_in_bound() == False or self.block_fits() == False:
            self.current_block.move(0, -1)
    
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_in_bound() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
        
    def lock_block(self):
        tiles = self.current_block.get_cell_pos()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_row()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    def play_game_over(self):
        if not self.game_over_sound_played:
            pygame.mixer.music.stop()
            self.game_over_sound.play()
            self.game_over_sound_played = True
    
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), 
                       TBlock(), ZBlock() ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.game_over_sound_played = False
    
    def block_fits(self):
        tiles = self.current_block.get_cell_pos()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.col) ==False:
                return False
        return True

    def block_in_bound(self):
        tiles = self.current_block.get_cell_pos()
        for tile in tiles:
            if self.grid.in_bound(tile.row, tile.col) == False:
                return False
        return True
        
    def rotate(self):
        self.current_block.rotate()
        if self.block_in_bound() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3: # i-block
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4: # i-block
            self.next_block.draw(screen, 255, 280)  
        else:
            self.next_block.draw(screen, 270, 270) 

import pygame 
from grid import Grid
from blocks import *

pygame.init()

# Defintions --> defines the variables needed

screen = pygame.display.set_mode((300, 600)) # width * height
pygame.display.set_caption("Tetris") #Title
clock = pygame.time.Clock() #control the speed of the game
dark_blue = (44, 44, 127)
game_grid = Grid()
block = LBlock()



# Game Loop --> updates the positions of game objects

while True:
    #get all the events in the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #draw
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)


    pygame.display.update() #updated the screen view
    clock.tick(60) #sets the game speed

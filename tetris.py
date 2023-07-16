import pygame 
from game import Game

pygame.init()

# Defintions --> defines the variables needed

screen = pygame.display.set_mode((300, 600)) # width * height
pygame.display.set_caption("Tetris") #Title
clock = pygame.time.Clock() #control the speed of the game
dark_blue = (44, 44, 127)
game = Game()
GAME_UPDATE = pygame.USEREVENT #creates event triggered if blk pos needs update
pygame.time.set_timer(GAME_UPDATE, 200)

# Game Loop --> updates the positions of game objects

while True:
    #get all the events in the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()
            

    #draw
    screen.fill(dark_blue)
    game.draw(screen)


    pygame.display.update() #updated the screen view
    clock.tick(60) #sets the game speed

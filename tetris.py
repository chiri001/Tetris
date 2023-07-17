import pygame 
from game import Game
from color import Color

pygame.init()
title_font = pygame.font.Font(None, 45)
score_surface = title_font.render("Score", True, Color.white)
next_surface = title_font.render("Next", True, Color.white)
game_over_surface = title_font.render("GAME OVER!", True, Color.red)

score_rect = pygame.Rect(330, 55, 170, 60)
next_rect = pygame.Rect(330, 215, 170, 180)

# Defintions --> defines the variables needed

screen = pygame.display.set_mode((520, 620)) # width * height
pygame.display.set_caption("Tetris") #Title
clock = pygame.time.Clock() #control the speed of the game
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
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
            

    #draw
    score_val_surface = title_font.render(str(game.score), True, Color.green)

    screen.fill(Color.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        game.play_game_over()
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    pygame.draw.rect(screen, Color.light_blue, score_rect, 0, 10)
    score_val_rect = score_val_surface.get_rect(centerx = score_rect.centerx,
                                                centery = score_rect.centery)
    screen.blit(score_val_surface, score_val_rect)
    pygame.draw.rect(screen, Color.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()  # updated the screen view
    clock.tick(60)  # sets the game speed

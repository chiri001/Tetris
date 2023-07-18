import pygame 
from game import Game
from color import Color

pygame.init()
title_font = pygame.font.Font(None, 45)
score_surface = title_font.render("Score", True, Color.white)
next_surface = title_font.render("Next", True, Color.white)
game_over_surface = title_font.render("GAME OVER!", True, Color.red)
button_font = pygame.font.Font(None, 50)
button_surface = button_font.render("RESTART", True, Color.white)


score_rect = pygame.Rect(330, 55, 170, 60)
next_rect = pygame.Rect(330, 215, 170, 180)
button_rect = pygame.Rect(330, 520, 170, 40)

# Defintions --> defines the variables needed

screen = pygame.display.set_mode((520, 620)) # width * height
pygame.display.set_caption("Tetris") #Title
clock = pygame.time.Clock() #control the speed of the game
GAME_UPDATE = pygame.USEREVENT #creates event triggered if blk pos needs update

def draw_button(screen, message, x, y, w, h, ic, ac, action=None):
    # ic is inactive color, ac is active color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: #check mouse is within rect
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            return action()   
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    small_text = pygame.font.Font(None, 25)
    text_surf, text_rect = text_objects(message, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)

def text_objects(text, font):
    text_surface = font.render(text, True, Color.white)
    return text_surface, text_surface.get_rect()

def easy_mode():
    pygame.time.set_timer(GAME_UPDATE, 350)
    return "easy"

def medium_mode():
    pygame.time.set_timer(GAME_UPDATE, 250)
    return "medium"

def hard_mode():
    pygame.time.set_timer(GAME_UPDATE, 100)
    return "hard"

def main_menu():
    menu = True
    game_start = False
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                SystemExit

        screen.fill(Color.dark_blue)
        difficulty = None
        difficulty = draw_button(screen, "Easy", 210, 200, 100, 50, Color.purple, Color.green, easy_mode)
        difficulty = difficulty or draw_button(screen, "Medium", 210, 260, 100, 50, Color.purple, Color.green, medium_mode)
        difficulty = difficulty or draw_button(screen, "Hard", 210, 320, 100, 50, Color.purple, Color.green, hard_mode)

        if difficulty:
            game_start = True
            menu = False

        pygame.display.update()
        clock.tick(15)

    return game_start

game_start = main_menu()
game = Game()


# Game Loop --> updates the positions of game objects

while True:
    #get all the events in the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN and game.game_over:
            mouse_pos = event.pos  # gets mouse position
            if button_rect.collidepoint(mouse_pos):
                game.game_over = False
                game.reset()

        if event.type == pygame.KEYDOWN:
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
        pygame.draw.rect(screen, Color.green, button_rect, 0, 10)
        screen.blit(button_surface, 
                    button_surface.get_rect(center=button_rect.center))
    
    pygame.draw.rect(screen, Color.light_blue, score_rect, 0, 10)
    score_val_rect = score_val_surface.get_rect(centerx = score_rect.centerx,
                                                centery = score_rect.centery)
    screen.blit(score_val_surface, score_val_rect)
    pygame.draw.rect(screen, Color.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()  # updated the screen view
    clock.tick(60)  # sets the game speed

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()   #initializes the bacground settings that pygame needs to work.
    ai_settings = Settings()
    screen = pygame.display.set_mode(   #displays a window which we draw all game graphical elements.the arguments are tuples which specify the dimensions of game
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    #make group to store bullets
    bullets = Group()

    #start of main loop for the game
    while True:
        # watch for mouse and keyboard events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #delete bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship,bullets)

run_game()
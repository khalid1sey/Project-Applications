import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached"""
    if len(bullets) < ai_settings.bullets_allowed:
        #create a new bullet and add it to bulet group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event, ship):
    """Respond to keyreleases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypressses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
         
def update_screen(ai_settings, screen, ship, alien, bullets):
    """Update images on the screen and fl        nip to the new screen."""
    screen.fill(ai_settings.bg_color)
    #redraw bullets behind ship and aliens
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    ship.blitme()
    alien.draw(screen)
     #make most recently drawn screen visible.
    pygame.display.flip()   #updates screen to starting state

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    #update bullet positions
    bullets.update()

    #delete bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine no of rows of aliens that fit on screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in arow """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_aliens_x = int(available_space_x / (2 * alien_width))
    return numbers_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens """
    #create an alien and find numbers of aliens in a row
    #Spacing bn each alien is equal to one alien width
   
    alien = Alien(ai_settings, screen)
    numbers_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    numer_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Create the first row of aliens
    for numer_rows in range(numer_rows):
        for alien_number in range(numbers_aliens_x):
            #create an alien and place it in row
            create_alien(ai_settings, screen, aliens, alien_number)
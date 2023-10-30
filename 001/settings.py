

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the gam's settings."""
        #screen settings
        self.screen_width = 1356
        self.screen_height = 700
        self.bg_color = (255,255, 255)

        #ship
        self.ship_speed_factor = 10

        #bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3    #limit numer of bullets

        #alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_directin of 1 represents right; -1 represents left.
        self.fleet_direction = 1


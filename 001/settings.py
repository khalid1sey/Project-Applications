

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the gam's settings."""
        #screen settings
        self.screen_width = 1356
        self.screen_height = 700
        self.bg_color = (210,210, 230)

        #ship
        self.ship_speed_factor = 1.5

        #bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3    #limit numer of bullets


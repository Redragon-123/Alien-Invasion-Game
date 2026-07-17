import pygame

class Settings:
    """Store all the settings for the game."""
    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230) 
        #Bullet settings
        self.bullet_speed = 6.0
        #Ship settings
        self.ship_speed= 5.5
        self.ship_speed_back_up = 5.5
        self.ship_shift_speed = 15.0
        self.shift_countdown_start_time = 0
        self.shift_start_time = 0
        self.shift_last = 100
        self.shift_countdown = 1500
        self.is_shifting = False
        self.is_shift_countdown = False
        #Alien settings
        self.alien1_speed = 1.0
        self.alien2_speed = 1.5
        self.alien3_speed = 0.5
        self.alien3_bullet_speed = 3.0
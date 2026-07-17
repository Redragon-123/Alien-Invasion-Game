import pygame

class Reload:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.is_reloading = False
        self.start_time = 0
        self.reload_time = 500
        
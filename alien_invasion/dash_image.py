import pygame 

class Dash_image:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/dash.png")
        self.rect = self.image.get_rect()

    def draw_dash_image(self):
        self.screen.blit(self.image,(0,690))
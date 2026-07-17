import pygame
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self, ai_game, pos):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.screen
        self.image = pygame.image.load("images/heart.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
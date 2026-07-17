import pygame
from pygame.sprite import Sprite

class Bullet_image(Sprite):
    def __init__(self, ai_game, pos):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
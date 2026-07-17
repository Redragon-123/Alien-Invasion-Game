import pygame
from pygame.sprite import Sprite

class Bullet_of_alien3(Sprite):
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/bullet2.png")
        self.image = pygame.transform.flip(self.image, False, True)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.midtop = alien.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien3_bullet_speed
        self.rect.y = self.y
        if self.rect.top >= self.settings.screen_height:
            self.kill()
    
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
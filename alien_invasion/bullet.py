import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        """Create a bullet object at the current position of the ship."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Create a bullet rect at (0,0) and the set to the correct position.
        self.image = pygame.image.load("images/laserBullet.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        #Store a float in y.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y-= self.settings.bullet_speed #Update the decimal position of the bullet.
        self.rect.y = self.y #Update the rect position.
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
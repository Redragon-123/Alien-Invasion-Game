import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen #Get the screen object from the AlienInvasion instance to draw the ship on it.
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect() #Get the rect of the screen to position the ship.
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/DurrrSpaceShip.png')
        self.rect = self.image.get_rect() # Get the rect of the ship image.
        #Put each new ships at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float in x.
        self.x = float(self.rect.x)
        #Signal of the movement.
        self.moving_right = False
        self.moving_left =  False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the position of the ship based on the movement signal."""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top>0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect. bottom<self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        
        #Update rect from x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
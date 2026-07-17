import pygame

class Button1:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width, self.height = 400, 100
        self.button_color = (0, 0, 180)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 72)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midtop = self.screen_rect.center
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Button2:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width, self.height = 400, 100
        self.button_color = (0, 0, 180)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 72)
        self.rect = pygame.Rect(400, 550, self.width, self.height)
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Button3:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width, self.height = 400, 100
        self.button_color = (0, 0, 180)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 72)
        self.rect = pygame.Rect(400, 700, self.width, self.height)
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

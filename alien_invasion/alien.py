import pygame 
from pygame.sprite import Sprite
import random
from bullet_of_alien3 import Bullet_of_alien3

class Alien1(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image1 = pygame.image.load("images/spiked ship 3. small.blue_.PNG")
        self.image1 = pygame.transform.flip(self.image1, False, True)
        self.image1 = pygame.transform.scale(self.image1,(70,70))
        self.rect = self.image1.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.x1 = float(self.rect.x)
        self.y1 = float(self.rect.y)
        self.direction = random.choice([-1,1])
        self.change_time = random.randint(30, 90)
        self.frame_count = 0
        self.speed = random.uniform(1.0, 1.5)
        self.left_limit1 = self.rect.width / 2
        self.right_limit1 = self.settings.screen_width - self.rect.width / 2
        self.count_start = 0
        self.alien1_refresh = 6000

    def update(self):
        self.y1 += self.settings.alien1_speed
        self.rect.y = self.y1
        self.frame_count += 1
        if self.frame_count >= self.change_time:
            self.direction *= -1
            self.frame_count = 0
        self.x1 += self.direction * self.speed
        if self.x1 < self.left_limit1:
            self.x1 = self.left_limit1
            self.direction = 1
        if self.x1 > self.right_limit1:
            self.x1 = self.right_limit1
            self.direction = -1
        self.rect.x = self.x1

class Alien2(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image2 = pygame.image.load("images/cartoonship green.png")
        self.image2 = pygame.transform.flip(self.image2, False, True)
        self.image2 = pygame.transform.scale(self.image2,(70,70))
        self.rect = self.image2.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.x2 = float(self.rect.x)
        self.y2 = float(self.rect.y)
        self.direction = random.choice([-1,1])
        self.change_time = random.randint(30, 90)
        self.frame_count = 0
        self.speed = random.uniform(1.0, 1.5)
        self.left_limit2 = self.rect.width / 2
        self.right_limit2 = self.settings.screen_width - self.rect.width / 2
        self.alpha = 255
        self.is_fading = False
        self.is_fading_over = True
        self.fade_start_time = 0
        self.fade_countdown_start = 0
        self.fade_countdown = 2000
        self.fade_last = 1000
        self.count_start = 0
        self.alien2_refresh = 7000

    def update(self):
        self.y2 += self.settings.alien2_speed
        self.rect.y = self.y2
        self.frame_count += 1
        if self.frame_count >= self.change_time:
            self.direction *= -1
            self.frame_count = 0
        self.x2 += self.direction * self.speed
        if self.x2 < self.left_limit2:
            self.x2 = self.left_limit2
            self.direction = 1
        if self.x2 > self.right_limit2:
            self.x2 = self.right_limit2
            self.direction = -1
        self.rect.x = self.x2
        self.update2_fade()

    def update2_fade(self):
        if self.is_fading_over and self.fade_countdown_start == 0:
            self.fade_countdown_start = pygame.time.get_ticks()
        current_countdown_time = pygame.time.get_ticks()
        if self.is_fading_over and current_countdown_time - self.fade_countdown_start >= self.fade_countdown:
            self.is_fading = True
            self.fade_countdown_start = 0
        if self.is_fading and self.fade_start_time == 0:
            self.fade_start_time = pygame.time.get_ticks()
            self.is_fading_over = False
        current_time = pygame.time.get_ticks()
        if self.is_fading and current_time - self.fade_start_time <= self.fade_last:
            self.alpha = 0
        if self.is_fading and current_time - self.fade_start_time > self.fade_last:
            self.alpha = 255
            self.is_fading = False
            self.is_fading_over = True
            self.fade_start_time = 0
        self.image2.set_alpha(self.alpha)
        
class Alien3(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image3 = pygame.image.load("images/ship4.png")
        self.image3 = pygame.transform.flip(self.image3, False, True)
        self.image3 = pygame.transform.scale(self.image3,(70,70))
        self.rect = self.image3.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.x3 = float(self.rect.x)
        self.y3 = float(self.rect.y)
        self.direction = random.choice([-1,1])
        self.change_time = random.randint(30, 90)
        self.frame_count = 0
        self.speed = random.uniform(1.0, 1.5)
        self.left_limit3 = self.rect.width / 2
        self.right_limit3 = self.settings.screen_width - self.rect.width / 2
        self.fire_start_time = 0
        self.fire_time = 2500
        self.count_start = 0
        self.alien3_refresh = 6500

    def update(self):
        self.y3 += self.settings.alien3_speed
        self.rect.y = self.y3
        self.frame_count += 1
        if self.frame_count >= self.change_time:
            self.direction *= -1
            self.frame_count = 0
        self.x3 += self.direction * self.speed
        if self.x3 < self.left_limit3:
            self.x3 = self.left_limit3
            self.direction = 1
        if self.x3 > self.right_limit3:
            self.x3 = self.right_limit3
            self.direction = -1
        self.rect.x = self.x3
        self.add_bullet()
    
    def add_bullet(self):
        if self.fire_start_time == 0:
            self.fire_start_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        if current_time - self.fire_start_time >= self.fire_time:
            new_bullet = Bullet_of_alien3(self.ai_game, self)
            self.ai_game.alien3_bullets.add(new_bullet)
            self.fire_start_time = 0

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from bullet_image import Bullet_image
from reload import Reload
from sound import Sound
from dash_image import Dash_image
from alien import Alien1, Alien2, Alien3
from bullet_of_alien3 import Bullet_of_alien3
from heart import Heart
from button import Button1, Button2, Button3

class AlienInvasion:
    "Class to manage game sources and behavior."
    def __init__(self):
        "Initialize the game and create game resources."
        pygame.init()
        self.clock = pygame.time.Clock() #Create a clock object to manage the game's frame rate
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #Set the size of the game window
        """Use the code below to set the game window to full screen mode."""
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        """Pygame do not provide the method to quit the game by 'Q'."""
        pygame.display.set_caption("Alien Invasion") #Name the game window
        self.background = pygame.image.load("images/image5.jpg")
        self.ship = Ship(self)
        self.reload = Reload(self)
        self.sound = Sound(self)
        self.dash_image = Dash_image(self)
        self.play_button = Button1(self, "Play")
        self.exit_button = Button2(self, "Exit")
        self.retry_button = Button1(self, "Retry")
        self.back_to_title_button = Button2(self, "Back to title")
        self.back_to_game_button = Button3(self, "Back to game")
        self.alien1 = Alien1(self)
        self.alien2 = Alien2(self)
        self.alien3 = Alien3(self)
        self.alien1.count_start = pygame.time.get_ticks()
        self.alien2.count_start = pygame.time.get_ticks()
        self.alien3.count_start = pygame.time.get_ticks()
        self.bullets = pygame.sprite.Group() #Create an empty group to store bullets in it.
        self.bullets_image = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien3_bullets = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.heart1 = Heart(self,(0,670))
        self.heart2 = Heart(self,(50,670))
        self.heart3 = Heart(self,(100,670))
        self.hearts.add(self.heart1, self.heart2, self.heart3)
        self.sprite1 = Bullet_image(self,(940,650))
        self.sprite2 = Bullet_image(self,(980,650))
        self.sprite3 = Bullet_image(self,(1020,650))
        self.sprite4 = Bullet_image(self,(1060,650))
        self.sprite5 = Bullet_image(self,(1100,650))
        self.bullets_image.add(self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5)
        self.font1 = pygame.font.Font(None,48)
        self.font2 = pygame.font.Font(None,36)
        self.font3 = pygame.font.Font(None,48)
        self.font4 = pygame.font.Font(None,48)
        self.font5 = pygame.font.Font(None,48)
        self.score = 0
        self.game_active = False
        self.game_paused = False
        self.game_over = False
        "Set the background color."
        self.bg_color = self.settings.bg_color #Set the backgroud color to a light gray.(RED, GREEN, BLUE) values range from 0 to 255.
        self.sound.play_bg_music2()
        self.game_timer = 0

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                if not self.game_paused and not self.game_over:
                    self.ship.update()
                    self._alien_refresh()
                    self.aliens.update()
                    self.alien3_bullets.update()
                    self._alien_refresh_update()
                    self._update_bullets()
                    self._reload_bullets()
                    self._is_shift_ready()
                    self._shift_dash()
                    self._collision_judge()
                    self._game_over()
            else: 
                self.play_button.draw_button()
            self._update_screen()
            self.clock.tick(60) #60 frames per second.

    def _check_events(self):      
        "Watch for keyboard and mouse events." 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #pygame.QUIT is the event that occurs when the user ckicks the close button on the game window
                sys.exit() #Quit the game safely.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_button(mouse_pos)
    
    def _check_mouse_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            pygame.mixer.music.stop()
            self.sound.play_bg_music1()
            self.game_active = True
        elif self.exit_button.rect.collidepoint(mouse_pos) and not self.game_active:
            sys.exit()
        elif self.retry_button.rect.collidepoint(mouse_pos) and (self.game_paused or self.game_over):
            self._reset_game()
            self.game_paused = False
        elif self.back_to_title_button.rect.collidepoint(mouse_pos) and (self.game_paused or self.game_over):
            self._reset_game()
            pygame.mixer.music.stop()
            self.sound.play_bg_music2()
            self.game_paused = False
            self.game_active = False
        elif self.back_to_game_button.rect.collidepoint(mouse_pos) and self.game_paused:
            self.game_paused = False
    
    def _check_keydown_events(self, event):
        """Respond to the key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right =True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True 
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.reload.is_reloading = False
            self.reload.start_time = 0
        elif event.key == pygame.K_r:
            self.reload.is_reloading = True
        elif event.key == pygame.K_LSHIFT:
            self.settings.is_shifting = True
        elif event.key == pygame.K_ESCAPE:
            if not self.game_over:
                self.game_paused = not self.game_paused

    def _check_keyup_events(self,event):
        """Respond to the key releases."""
        if event.key ==pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False
    
    def _reset_game(self):
        self.game_over = False
        self.game_paused = False
        self.aliens.empty()
        self.bullets.empty()
        self.alien3_bullets.empty()
        self.hearts.empty()
        self.hearts.add(self.heart1, self.heart2, self.heart3)
        self.bullets_image.empty()
        self.bullets_image.add(self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5)
        self.ship.center_ship()
        self.score = 0
        current_time = pygame.time.get_ticks()
        self.game_timer = current_time
        self.alien1.count_start = current_time
        self.alien2.count_start = current_time
        self.alien3.count_start = current_time


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if self.bullets_image and not self.game_paused and not self.game_over:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            last_bullet_image = self.bullets_image.sprites()[-1]
            self.bullets_image.remove(last_bullet_image)
            self.sound.play_sound_fire()
    
    def _reload_bullets(self):
        """Reload the bullets when the player presses 'R'."""
        if self.reload.start_time == 0:
            self.reload.start_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        if self.reload.is_reloading and len(self.bullets_image) == 0:
            if current_time - self.reload.start_time >= self.reload.reload_time:
                self.bullets_image.add(self.sprite1)
                self.sound.play_sound_reload()
                self.reload.start_time = 0
        elif self.reload.is_reloading and len(self.bullets_image) == 1:
            if current_time - self.reload.start_time >= self.reload.reload_time:
                self.bullets_image.add(self.sprite2)
                self.sound.play_sound_reload()
                self.reload.start_time = 0
        elif self.reload.is_reloading and len(self.bullets_image) == 2:
            if current_time - self.reload.start_time >= self.reload.reload_time:
                self.bullets_image.add(self.sprite3)
                self.sound.play_sound_reload()
                self.reload.start_time = 0
        elif self.reload.is_reloading and len(self.bullets_image) == 3:
            if current_time - self.reload.start_time >= self.reload.reload_time:
                self.bullets_image.add(self.sprite4)
                self.sound.play_sound_reload()
                self.reload.start_time = 0
        elif self.reload.is_reloading and len(self.bullets_image) == 4:
            if current_time - self.reload.start_time >= self.reload.reload_time:
                self.bullets_image.add(self.sprite5)
                self.sound.play_sound_reload()
                self.reload.start_time = 0
        elif self.reload.is_reloading and len(self.bullets_image) == 5:
            self.reload.is_reloading = False
    
    def _alien_refresh_update(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.game_timer) % 20000 == 0:
            self.alien1.alien1_refresh -= 500
            self.alien2.alien2_refresh -= 500
            self.alien3.alien3_refresh -= 500
        if self.alien1.alien1_refresh <= 500:
            self.alien1.alien1_refresh = 500
        if self.alien2.alien2_refresh <= 1000:
            self.alien2.alien2_refresh = 1000
        if self.alien3.alien3_refresh <= 1000:
            self.alien3.alien3_refresh = 1000
    
    def _alien_refresh(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.alien1.count_start) >= self.alien1.alien1_refresh:
            new_alien = Alien1(self)
            self.aliens.add(new_alien)
            self.alien1.count_start = current_time
        if (current_time - self.alien2.count_start) >= self.alien2.alien2_refresh:
            new_alien = Alien2(self)
            self.aliens.add(new_alien)
            self.alien2.count_start = current_time
        if (current_time - self.alien3.count_start) >= self.alien3.alien3_refresh:
            new_alien = Alien3(self)
            self.aliens.add(new_alien)
            self.alien3.count_start = current_time

    def _update_bullets(self):
        """Update position of bullets and get rid of the old bullets."""
        self.bullets.update()
        #Get the rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _draw_text(self):
        text = f"Press 'R' to reload."
        text_image = self.font1.render(text, True, (255,255,255))
        text_rect = text_image.get_rect()
        text_rect.bottomright = self.screen.get_rect().bottomright
        self.screen.blit(text_image, text_rect)

    def _draw_bullet_reloading(self):
        text = f"Reloading..."
        text_image = self.font2.render(text, True, (255,255,255))
        text_rect = text_image.get_rect()
        text_rect.bottomleft = self.sprite1.rect.topleft
        self.screen.blit(text_image, text_rect)
    
    def _draw_charging(self):
        text = f"Charging..."
        text_image = self.font3.render(text, True, (255,255,255))
        text_rect = text_image.get_rect()
        text_rect.bottomleft = self.screen.get_rect().bottomleft
        self.screen.blit(text_image, text_rect)

    def _draw_firing(self):
        text = f"Press 'Space' to fire."
        text_image = self.font4.render(text, True, (255,255,255))
        text_rect = text_image.get_rect()
        text_rect.midbottom = self.screen.get_rect().midbottom
        self.screen.blit(text_image, text_rect)
    
    def _draw_score(self):
        text = f"Score:{self.score}"
        text_image = self.font5.render(text, True, (255,255,255))
        text_rect = text_image.get_rect()
        text_rect.topleft = self.screen.get_rect().topleft
        self.screen.blit(text_image, text_rect)

    def _is_shift_ready(self):
        if self.settings.is_shift_countdown == False:
            current_time = pygame.time.get_ticks()
            if self.settings.shift_countdown_start_time == 0:
                self.settings.shift_countdown_start_time = pygame.time.get_ticks()
            if current_time - self.settings.shift_countdown_start_time >= self.settings.shift_countdown:
                self.settings.is_shift_countdown = True
                self.settings.shift_countdown_start_time = 0

    def _shift_dash(self):
        if self.settings.is_shift_countdown == True and self.settings.is_shifting == True:
            current_time = pygame.time.get_ticks()
            if self.settings.shift_start_time == 0:
                self.settings.shift_start_time = pygame.time.get_ticks()
            if current_time - self.settings.shift_start_time <= self.settings.shift_last:
                self.settings.ship_speed = self.settings.ship_shift_speed
            else:
                self.settings.ship_speed = self.settings.ship_speed_back_up
                self.settings.is_shift_countdown = False
                self.settings.is_shifting = False
                self.settings.shift_start_time = 0
        else:
            self.settings.is_shifting = False
    
    def _collision_judge(self):
        collision1 = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collision1:
            self.score += 1
            self.sound.play_sound_explosion()
        collision2 = pygame.sprite.groupcollide(self.bullets, self.alien3_bullets, True, True)
        if pygame.sprite.spritecollideany(self.ship, self.alien3_bullets):
            hit_bullet = pygame.sprite.spritecollideany(self.ship, self.alien3_bullets)
            if self.hearts.sprites():
                last_heart = self.hearts.sprites()[-1]
                self.hearts.remove(last_heart)
            self.alien3_bullets.remove(hit_bullet)
            self.sound.play_sound_hurt()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            hit_alien = pygame.sprite.spritecollideany(self.ship, self.aliens)
            if self.hearts.sprites():
                last_heart = self.hearts.sprites()[-1]
                self.hearts.remove(last_heart)
            self.aliens.remove(hit_alien)
            self.score += 1
            self.sound.play_sound_explosion()
            self.sound.play_sound_hurt()
        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.settings.screen_height:
                if self.hearts.sprites():
                    last_heart = self.hearts.sprites()[-1]
                    self.hearts.remove(last_heart)
                self.aliens.remove(alien)
    
    def _game_over(self):
        if not self.hearts:
            self.game_over = True

    def _update_screen(self):            
        "Redraw the screen each time through the loop."
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background,(0,0))
        self.bullets_image.draw(self.screen)
        self._draw_text()
        self._draw_firing()
        self._draw_score()
        self.hearts.draw(self.screen)
        if self.reload.is_reloading:
            self._draw_bullet_reloading()
        if self.settings.is_shift_countdown == False:
            self._draw_charging()
        if self.settings.is_shift_countdown:
            self.dash_image.draw_dash_image()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            if isinstance(alien, Alien1):
                self.screen.blit(alien.image1, alien.rect)
            elif isinstance(alien, Alien2):
                self.screen.blit(alien.image2, alien.rect)
            elif isinstance(alien, Alien3):
                self.screen.blit(alien.image3, alien.rect)
                for bullet in self.alien3_bullets.sprites():
                    bullet.draw_bullet()
        self.ship.blitme()
        if self.game_paused:
            self._draw_paused_screen()
            self.retry_button.draw_button()
            self.back_to_title_button.draw_button()
            self.back_to_game_button.draw_button()
        if self.game_over:
            self._draw_game_over_screen()
            self.retry_button.draw_button()
            self.back_to_title_button.draw_button()
        if not self.game_active:
            self._draw_title()
            self.play_button.draw_button()
            self.exit_button.draw_button()
        "Redraw the screen during each pass through the loop."
        pygame.display.flip()
    
    def _draw_paused_screen(self):
        pause_overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        pause_overlay.fill((0, 0, 0, 150))
        self.screen.blit(pause_overlay, (0, 0))
        title_font = pygame.font.Font(None, 100)
        image = title_font.render("PAUSED", True, (255, 255, 255))
        rect = image.get_rect(midbottom = self.screen.get_rect().center)
        self.screen.blit(image, rect)
    
    def _draw_game_over_screen(self):
        over_overlay = pygame.Surface((1200, 800))
        over_overlay.fill((0,0,0))
        self.screen.blit(over_overlay, (0,0))
        title_font = pygame.font.Font(None, 100)
        image = title_font.render("Game Over", True, (255,255,255))
        rect = image.get_rect(midbottom = self.screen.get_rect().center)
        self.screen.blit(image, rect)
    
    def _draw_title(self):
        title_overlay = pygame.Surface((1200, 800))
        title_overlay.fill((0,0,0))
        self.screen.blit(title_overlay, (0,0))
        title_font = pygame.font.Font(None, 150)
        image = title_font.render("Alien Invasion", True, (255,255,255))
        rect = image.get_rect(midbottom = self.screen.get_rect().center)
        self.screen.blit(image, rect)

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai=AlienInvasion()
    ai.run_game()
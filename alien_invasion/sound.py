import pygame

class Sound:
    def __init__(self, ai_game):
        pygame.mixer.init()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bg_music1_path = "sound/death_-_w4ck_punk_rock_metal_heavy_badass.mp3"
        self.bg_music2_path = "sound/Space Background Music.mp3"
        self.sound_fire = pygame.mixer.Sound("sound/8bit_gunloop_explosion.wav")
        self.sound_reload = pygame.mixer.Sound("sound/outofammo.wav")
        self.sound_explosion = pygame.mixer.Sound("sound/explosion.wav")
        self.sound_hurt = pygame.mixer.Sound("sound/pumpkin_break_01.ogg")
    
    def play_bg_music1(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(self.bg_music1_path)
        pygame.mixer.music.play(-1)

    def play_bg_music2(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(self.bg_music2_path)
        pygame.mixer.music.play(-1)
    
    def play_sound_fire(self):
        self.sound_fire.set_volume(0.5)
        self.sound_fire.play()

    def play_sound_reload(self):
        self.sound_reload.set_volume(0.5)
        self.sound_reload.play()
    
    def play_sound_explosion(self):
        self.sound_explosion.set_volume(0.5)
        self.sound_explosion.play()
    
    def play_sound_hurt(self):
        self.sound_hurt.set_volume(0.5)
        self.sound_hurt.play
import pygame

class Level:
    def __init__(self):
        
        # grouping of sprites 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
    def run(self):
        #update game window
        pass
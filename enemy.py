import pygame
import random

from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((20, 20), flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(random.randint(15, W-15), random.randint(15, H-15)))
        self.radius = 10
        self.color = (67, 87, 95)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

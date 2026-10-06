import pygame

from config import *

class Segment(pygame.sprite.Sprite):
    """It's a segment of a snake"""
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface((26, 26)) # its image and rect
        self.image.fill((0, 56, 76))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.pos = pygame.math.Vector2(self.rect.center) # position of its center

    def move(self, new_position):
        self.pos = new_position
        self.rect.center = (round(self.pos.x), round(self.pos.y)) # so then we move we just change our position

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.segments = [Segment(W//2, H//2)] # all our segments
        
        self.cell = 26 # cell size - how much do we move in one period of time
        self.timer = 0
        self.time = 0.3
        self.direction = pygame.math.Vector2(1, 0) # our base direction - it's for the head
        self.alive = True
        
    def grow(self):
        last_segment = self.segments[-1]
        new_segment = Segment(last_segment.rect.centerx, last_segment.rect.centery)
        self.segments.append(new_segment) # we make new segment and its position is a position of latest but it will change in move() method because the latest one also will change it's position
        self.time -= 0.01 if self.time > 0.05 else 0 # and we make the game a bit harder
        
    def draw(self, screen):
        for seg in self.segments:
            screen.blit(seg.image, seg.rect)  # we here draw all our segments      
        
    def move(self):
        old_pos = [seg.pos for seg in self.segments] # our current positions
        
        head = self.segments[0]
        new_pos = head.pos + self.direction*self.cell
        head.move(new_pos) # we move one head on position new_pos
        
        for i in range(1, len(self.segments)):
            self.segments[i].move(old_pos[i-1]) # now we move every segment on the next one's position
        
    def handle_input(self):
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_DOWN] and self.direction.y == 0:
            self.direction = pygame.math.Vector2(0, 1)   # we make the new vector because we can
        elif keys[pygame.K_UP] and self.direction.y == 0:
            self.direction = pygame.math.Vector2(0, -1)
        elif keys[pygame.K_LEFT] and self.direction.x == 0:
            self.direction = pygame.math.Vector2(-1, 0) 
        elif keys[pygame.K_RIGHT] and self.direction.x == 0:
            self.direction = pygame.math.Vector2(1, 0) 
            
    def die(self):
        self.alive = False
        
    def update(self, dt):
        if not self.alive:
            return
        
        self.handle_input()        
        self.timer += dt
        
        if self.timer >= self.time: # so every self.time seconds our timer will tik and we move
            self.move()
            self.timer = 0
            
            self.check_wall_collision()
            self.check_self_collision()

            
    def check_wall_collision(self):
        head = self.segments[0]
        if head.rect.y < 0 or head.rect.y > H-26 or head.rect.x < 0 or head.rect.x > W-26:
            self.die()
            
    def check_self_collision(self):
        head_center = self.segments[0].rect.center

        for seg in self.segments[1:]:
            if seg.rect.collidepoint(head_center): # only check if head and another segment are collided
                self.die()
                return # we break the cycle!

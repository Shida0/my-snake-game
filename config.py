import pygame

pygame.init()

H = 720
W = 1280
score_font = pygame.font.Font(None, 36)
die_font = pygame.font.Font(None, 100)

class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback 
        self.font = pygame.font.Font(None, 70)
        self.color = (255, 255, 255)
        self.bg_color = (89, 60, 56)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if self.rect.collidepoint(event.pos):
                self.callback()
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        text_surf = self.font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
        

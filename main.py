import sys
import pygame

from config import *
from snake import Snake
from enemy import Enemy

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

snake = Snake() # snake and enemy
enemy = Enemy()

enemies = pygame.sprite.Group() # groups
all_sprites = pygame.sprite.Group()
all_sprites.add(enemy)
enemies.add(enemy)

score_text = 0

# restart function
def restart():
    global score_text, snake, all_sprites, enemy
    
    score_text = 0
    
    snake = Snake()
    enemy = Enemy()
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(enemy)
    enemies.add(enemy)
    
restart_btn = Button(W//2-100, H//2+100, 200, 70, "Restart", restart)

while True:
    dt = clock.tick(60)/1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        restart_btn.handle_event(event) # handle if we click on this button
            
    all_sprites.update(dt)    
    snake.update(dt)    # update enemies and snake
           
    screen.fill((0, 0, 0))    
    all_sprites.draw(screen)
    snake.draw(screen) # draw all
    
    score = score_font.render(f"{score_text}", True, (255, 255, 255))
    screen.blit(score, (25, 25)) # update score
    
    if snake.alive == False:
        die_text = die_font.render("You died!", True, (255, 255, 255))
        rect = die_text.get_rect(center=(W//2, H//2))
        screen.blit(die_text, rect)
        restart_btn.draw(screen) # die functional
        

    seg = snake.segments[0]
    hits = pygame.sprite.spritecollide(seg, enemies, dokill=True) # if we hit some enemy    
    if hits:
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        score_text += 1     
        snake.grow()       
    
    pygame.display.update()

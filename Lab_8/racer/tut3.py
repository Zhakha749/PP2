import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W, H = 400, 600
SPEED = 5
SCORE = 0

font = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_8\racer\font_user (1).ttf", 60)
font_small = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_8\racer\font_user (1).ttf", 20)
game_over = font.render("Game Over", True, BLACK)

bg = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_8\racer\AnimatedStreet.png")

SC = pygame.display.set_mode((W, H))
SC.fill(WHITE)
pygame.display.set_caption("My game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_8\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_8\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1
        
        if event.type == QUIT:
            pygame.quit()
            exit()

    SC.blit(bg, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    SC.blit(scores, (10, 10))

    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, enemies):
    #if P1.rect.colliderect(E1.rect) and abs(P1.rect.centerx - E1.rect.centerx) < 5:
        pygame.mixer.Sound(r"C:\Users\user\Desktop\PP2\Lab_8\racer\crash.wav").play()
        time.sleep(0.5)

        SC.fill(RED)
        SC.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)
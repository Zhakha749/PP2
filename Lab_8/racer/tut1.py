import pygame
from pygame.locals import *
import random

pygame.init()

FPS = 60
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W, H = 400, 600
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
        self.rect.move_ip(0, 10)
        if(self.rect.bottom>600):
            self.rect.top=0
            self.rect.center = (random.randint(30, 370), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_8\racer\Player.png"
        )
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def update(self):
        pressed_kays = pygame.key.get_pressed()
        '''if pressed_kays[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_kays[K_DOWN]:
            self.rect.move_ip(0, 5)'''
        
        if self.rect.left > 0:
            if pressed_kays[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < W:
            if pressed_kays[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    P1.update()
    E1.move()

    SC.fill(WHITE)
    P1.draw(SC)
    E1.draw(SC)

    pygame.display.update()
    clock.tick(FPS)

import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size and initial values
W, H = 400, 600
SPEED = 5
SCORE = 0
COINS = 0

# Load fonts and render "Game Over" text
font = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_9\racer\font_user (1).ttf", 60)
font_small = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_9\racer\font_user (1).ttf", 20)
game_over = font.render("Game Over", True, BLACK)

# Load and resize coin icon
coin_icon = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_9\racer\coin.png")
coin_icon = pygame.transform.scale(coin_icon, (coin_icon.get_width()//20, coin_icon.get_height()//20))

# Load background image
bg = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_9\racer\AnimatedStreet.png")

# Create display surface
SC = pygame.display.set_mode((W, H))
SC.fill(WHITE)
pygame.display.set_caption("My game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_9\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    # Move enemy down, reset and increase score when it exits screen
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_9\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # Move left or right based on key press
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 1:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_9\racer\coin.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//12, self.image.get_height()//12))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    # Move coin downward and reset when it goes off screen
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

# Create player, enemy, and coin objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins_group = pygame.sprite.Group()
coins_group.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Speed increase event (commented out)
'''INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)'''

# Coin collection counter
count = 0

# Game loop
while True:
    for event in pygame.event.get():
        # Check for quit event
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Draw background
    SC.blit(bg, (0, 0))

    # Draw coin icon and current coin count
    SC.blit(coin_icon, (10, 35))
    coins_v = font_small.render(f"X{str(COINS)}", True, BLACK)
    SC.blit(coins_v, (50, 50))

    # Update and draw all sprites
    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)
        entity.move()

    # Check for collision between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\user\Desktop\PP2\Lab_9\racer\crash.wav").play()
        time.sleep(0.5)

        # Game over screen
        SC.fill(RED)
        SC.blit(game_over, (30, 250))
        result = font_small.render(f"Your result: {COINS}", True, BLACK)
        SC.blit(result, (120, 350))
        pygame.display.update()

        # Remove all sprites and exit
        for entity in all_sprites:
            entity.kill()
        
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Increase game speed after collecting coins
    if count > 5 and SPEED < 15:
        count = 0
        SPEED += 1

    # Check for collision between player and coin
    if pygame.sprite.spritecollideany(P1, coins_group):
        # Add random number of coins (1 to 3 or 4)
        COINS += random.randint(1, 4)
        count += COINS
        for i in coins_group:
            i.rect.top = 0
            i.rect.center = (random.randint(40, W-40), 0)

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

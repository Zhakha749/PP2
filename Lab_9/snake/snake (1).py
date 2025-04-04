import pygame
import random
import time

# Initial snake speed
snake_speed = 5

# Initialize Pygame
pygame.init()

# Window dimensions
W, H = 720, 480

# Defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Set window title and size
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((W, H))

# Create clock object to control FPS
FPS = pygame.time.Clock()

# Snake initial position and body
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Different food types with score values and lifetime (in seconds)
food_types = [
    {"color": RED, "score": 10, "lifetime": 5},     # common food
    {"color": BLUE, "score": 20, "lifetime": 4},    # rare food
    {"color": YELLOW, "score": 30, "lifetime": 3}   # very rare food
]

# Function to spawn a new fruit
def spawn_fruit():
    pos = [random.randrange(1, (W//10)) * 10, random.randrange(1, (H//10)) * 10]
    food = random.choice(food_types)
    spawn_time = time.time()
    return {"pos": pos, "type": food, "spawn_time": spawn_time}

# First food
fruit = spawn_fruit()

# Direction variables
direction = "RIGHT"
change_to = direction

# Score and food counter
score = 0
count_food = 0

# Function to display the score
def show_score(choice, color, font, size):
    score_font = pygame.font.Font(font, size)
    score_surf = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surf.get_rect()
    screen.blit(score_surf, score_rect)

# Function to end the game
def game_over():
    my_font = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_9\font_user (3).ttf", 30)
    game_over_surf = my_font.render("Your score is: " + str(score), True, RED)
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (W/4, H/4)
    screen.blit(game_over_surf, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Change direction with no reverse
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake in current direction
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10

    # Add new head position
    snake_body.insert(0, list(snake_pos))

    # Check if snake eats the fruit
    if snake_pos == fruit["pos"]:
        score += fruit["type"]["score"]
        count_food += 1
        fruit = spawn_fruit()  # spawn a new one
    else:
        # Remove tail segment if fruit not eaten
        snake_body.pop()

    # Check if fruit expired
    if time.time() - fruit["spawn_time"] > fruit["type"]["lifetime"]:
        fruit = spawn_fruit()

    # Drawing section
    screen.fill(BLACK)

    # Draw snake body
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw fruit
    pygame.draw.rect(screen, fruit["type"]["color"], pygame.Rect(fruit["pos"][0], fruit["pos"][1], 10, 10))

    # Game over if snake hits wall
    if snake_pos[0] < 0 or snake_pos[0] > W - 10 or snake_pos[1] < 0 or snake_pos[1] > H - 10:
        game_over()

    # Game over if snake collides with itself
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Speed up after eating 4 fruits
    if count_food == 4 and snake_speed < 24:
        snake_speed += 3
        count_food = 0

    # Display score
    show_score(1, PURPLE, r"C:\Users\user\Desktop\PP2\Lab_9\font_user (3).ttf", 20)
    pygame.display.update()
    FPS.tick(snake_speed)

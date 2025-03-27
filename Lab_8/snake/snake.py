import pygame
import random
import time

# Initial speed of the snake
snake_speed = 5

# Initialize Pygame
pygame.init()

# Screen dimensions
W, H = 720, 480

# Define RGB color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE= (128, 0, 128)

# Set the window title
pygame.display.set_caption("Snake Game")
# Set the game screen size
screen = pygame.display.set_mode((W, H))

# Clock object to control game frame rate
FPS = pygame.time.Clock()

# Initial position of the snake's head
snake_pos = [100, 50]
# Initial body segments of the snake
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Random position of the fruit (aligned to grid)
fruit_pos = [random.randrange(1, (W//10)) * 10, random.randrange(1, (H//10)) * 10]
# Flag to check if fruit should be spawned
fruit_spawn = True

# Initial direction
direction = "RIGHT"
# New direction input from user
change_to = direction

# Initial score
score = 0

# Function to show the current score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.Font(font, size)
    score_surf = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surf.get_rect()
    screen.blit(score_surf, score_rect)

# Function to handle game over state
def game_over():
    my_font = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_8\snake\font_user (2).ttf", 30)
    game_over_surf = my_font.render("Your score is: " + str(score), True, RED)
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (W/4, H/4)
    screen.blit(game_over_surf, game_over_rect)

    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

# Counter to track how many fruits were eaten (for speed-up logic)
count_food = 0

# Game loop
while True:
    # Event handling (keyboard input)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Prevent the snake from moving in the opposite direction instantly
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake head position based on direction
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10

    # Insert new head position into the snake's body list
    snake_body.insert(0, list(snake_pos))

    # If snake eats fruit
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        count_food += 1
        fruit_spawn = False  # trigger new fruit generation
    else:
        # Remove last segment of the body to simulate movement
        snake_body.pop()

    # Generate new fruit if needed
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (W//10)) * 10, random.randrange(1, (H//10)) * 10]
    fruit_spawn = True

    # Clear the screen
    screen.fill(BLACK)

    # Draw snake body
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the fruit
    pygame.draw.rect(screen, RED, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Game over conditions: hitting wall
    if snake_pos[0] < 0 or snake_pos[0] > W - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > H - 10:
        game_over()

    # Game over condition: hitting itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Increase speed after eating 4 fruits, up to a limit
    if count_food == 4 and snake_speed < 24:
        snake_speed += 3
        count_food = 0

    # Show score
    show_score(1, PURPLE, r"C:\Users\user\Desktop\PP2\Lab_8\snake\font_user (2).ttf", 20)

    # Refresh game screen
    pygame.display.update()

    # Control the game speed
    FPS.tick(snake_speed)

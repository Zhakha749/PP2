import pygame

# Initialize all imported pygame modules
pygame.init()

# Set up screen width and height
W, H = 900, 800
sc = pygame.display.set_mode((W, H))

# Define commonly used colors as RGB tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (252, 154, 8)
YELLOW = (252, 248, 3)
PINK = (252, 3, 252)
PURPLE = (169, 3, 252)
GRAY = (206, 204, 207)

# Map color names to RGB values for easy access
colors = {'white': WHITE, 'black': BLACK, 'red': RED, 'green': GREEN, 'blue': BLUE,
          'orange': ORANGE, 'yellow': YELLOW, 'pink': PINK, 'purple': PURPLE, 'gray': GRAY}

# Load and scale the eraser image for display
eraser = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_9\paint\eraser (1).png").convert_alpha()
eraser = pygame.transform.scale(eraser, (eraser.get_width()//15, eraser.get_height()//15))
eraser_rect = eraser.get_rect(center=(700, 70))  # Set eraser icon position
eraser2 = pygame.transform.scale(eraser, (eraser.get_width()//1.5, eraser.get_height()//1.5))  # Bigger eraser for cursor

# Initialize drawing settings
current_color = RED
mode = "brush"  # Can be: brush, rect, circle, rhombus, right_tr, eq_tr

drawed = []  # List to store all drawn shapes

# Fill background with white color
sc.fill(WHITE)

# Initialize mouse coordinates and other control variables
x, y = 0, 0
clock = pygame.time.Clock()
font = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_9\paint\font_user (4).ttf", 15)

is_erase = False  # Track if eraser mode is active
is_visible = True  # Control cursor visibility

start_pos = None  # Store starting position for shapes
preview_shape = None  # Store shape preview during drawing
drawing_rhombus = False  # Not used in current code logic

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # Exit if window is closed

        # Handle mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if a color button was clicked
            if color_yellow.collidepoint(event.pos):
                current_color = YELLOW
            elif color_green.collidepoint(event.pos):
                current_color = GREEN
            elif color_red.collidepoint(event.pos):
                current_color = RED
            elif color_blue.collidepoint(event.pos):
                current_color = BLUE
            elif color_orange.collidepoint(event.pos):
                current_color = ORANGE
            elif color_pink.collidepoint(event.pos):
                current_color = PINK
            elif color_purple.collidepoint(event.pos):
                current_color = PURPLE
            elif color_black.collidepoint(event.pos):
                current_color = BLACK
            # Toggle eraser mode
            elif eraser_rect.collidepoint(event.pos):
                is_visible = not is_visible
                is_erase = not is_erase
            # Change tool mode
            elif square_button.collidepoint(event.pos):
                mode = "rect"
            elif circle_button.collidepoint(event.pos):
                mode = "circle"
            elif rhombus_button.collidepoint(event.pos):
                mode = "rhombus"
            elif brush_button.collidepoint(event.pos):
                mode = "brush"
            elif right_tr_button.collidepoint(event.pos):
                mode = "right_tr"
            elif eq_tr_button.collidepoint(event.pos):
                mode = "eq_tr"
            # Start drawing based on mode
            elif event.pos[1] >= 183 and not is_erase:
                if mode in ("rect", "circle", "rhombus", "right_tr", "eq_tr"):
                    start_pos = event.pos
                elif mode == "brush":
                    drawed.append(("dot", event.pos, current_color))

        # Handle mouse release event to finalize shape
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and start_pos:
            end_pos = event.pos
            preview_shape = None
            drawed.append((mode, start_pos, end_pos, current_color))  # Save final shape
            start_pos = None

        # Handle mouse movement for drawing
        elif event.type == pygame.MOUSEMOTION:
            if start_pos and pygame.mouse.get_pressed()[0] and not is_erase:
                preview_shape = (mode, start_pos, event.pos, current_color)
            elif pygame.mouse.get_pressed()[0] and mode == "brush" and not is_erase and pygame.mouse.get_pos()[1] >= 183:
                drawed.append(("dot", pygame.mouse.get_pos(), current_color))

    # Clear screen before redrawing everything
    sc.fill(WHITE)

    # Draw all saved shapes
    for item in drawed:
        if item[0] == "dot":
            _, pos, color = item
            pygame.draw.circle(sc, color, pos, 5)
        else:
            fig_type, sp, ep, color = item
            x1, y1 = sp
            x2, y2 = ep
            centerx = (x1+x2)//2
            centery = (y1+y2)//2
            top = (centerx, y1)
            right = (x2, centery)
            bottom = (centerx, y2)
            left = (x1, centery)
            rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
            rect.normalize()
            # Draw based on shape type
            if fig_type == "rect":
                pygame.draw.rect(sc, color, rect)
            elif fig_type == "circle":
                center = rect.center
                radius = int(min(rect.width, rect.height) / 2)
                pygame.draw.circle(sc, color, center, radius)
            elif fig_type == "rhombus":
                pygame.draw.polygon(sc, color, [top, right, bottom, left])
            elif fig_type == "right_tr":
                pygame.draw.polygon(sc, color, [(x1, y1), (x2, y2), (x1, y2)])
            elif fig_type == "eq_tr":
                pygame.draw.polygon(sc, color, [(x1, y2), (x2, y2), ((x1+x2)//2, y2-abs(x2-x1))])

    # Draw preview while dragging shape
    if preview_shape:
        fig_type, sp, ep, color = preview_shape
        rect = pygame.Rect(*sp, ep[0] - sp[0], ep[1] - sp[1])
        rect.normalize()
        if fig_type == "rect":
            pygame.draw.rect(sc, color, rect, 2)
        elif fig_type == "circle":
            center = rect.center
            radius = int(min(rect.width, rect.height) / 2)
            pygame.draw.circle(sc, color, center, radius, 2)
        elif fig_type == "rhombus":
            pos = pygame.mouse.get_pos()
            centerx = (pos[0]+sp[0])//2
            centery = (pos[1]+sp[1])//2
            top = (centerx, sp[1])
            right = (pos[0], centery)
            bottom = (centerx, pos[1])
            left = (sp[0], centery)
            pygame.draw.polygon(sc, color, [top, right, bottom, left], 2)
        elif fig_type == "right_tr":
            pos = pygame.mouse.get_pos()
            pygame.draw.polygon(sc, color, [sp, pos, (sp[0], pos[1])], 2)
        elif fig_type == "eq_tr":
            pos = pygame.mouse.get_pos()
            pygame.draw.polygon(sc, color, [sp, pos, ((sp[0]+pos[0])//2, pos[1]-abs(pos[0]-sp[0]))])

    # Update mouse visibility
    pygame.mouse.set_visible(is_visible)

    # Handle eraser logic
    if is_erase:
        sc.blit(eraser2, pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            new_drawed = []
            for item in drawed:
                if item[0] == "dot":
                    pos, color = item[1], item[2]
                    dx = pos[0] - mx
                    dy = pos[1] - my
                    if (dx**2 + dy**2)**0.5 > 10:
                        new_drawed.append(item)
                else:
                    fig_type, sp, ep, color = item
                    rect = pygame.Rect(*sp, ep[0] - sp[0], ep[1] - sp[1])
                    rect.normalize()
                    # Remove shape if eraser overlaps it
                    if fig_type == "rect":
                        if not rect.collidepoint(mx, my):
                            new_drawed.append(item)
                    elif fig_type == "circle":
                        center = rect.center
                        radius = int(min(rect.width, rect.height) / 2)
                        dx = mx - center[0]
                        dy = my - center[1]
                        if dx**2 + dy**2 > radius**2:
                            new_drawed.append(item)
                    else:  # rough bounding box erase for other shapes
                        if (mx < min(sp[0], ep[0]) or mx > max(sp[0], ep[0])) and (my < min(sp[1], ep[1]) or my > max(sp[1], ep[1])):
                            new_drawed.append(item)
            drawed = new_drawed

    # Draw UI components: color buttons, tool icons, text
    # Display current color
    pygame.draw.rect(sc, GRAY, (50, 30, 130, 130), 5)
    pygame.draw.rect(sc, current_color, (55, 35, 120, 120))

    # Draw all color selection buttons
    color_red_border = pygame.draw.rect(sc, GRAY, (295, 25, 60, 60), 5)
    color_red = pygame.draw.rect(sc, RED, (300, 30, 50, 50))
    color_yellow_border = pygame.draw.rect(sc, GRAY, (375, 25, 60, 60), 5)
    color_yellow = pygame.draw.rect(sc, YELLOW, (380, 30, 50, 50))
    color_green_border = pygame.draw.rect(sc, GRAY, (455, 25, 60, 60), 5)
    color_green = pygame.draw.rect(sc, GREEN, (460, 30, 50, 50))
    color_blue_border = pygame.draw.rect(sc, GRAY, (535, 25, 60, 60), 5)
    color_blue = pygame.draw.rect(sc, BLUE, (540, 30, 50, 50))
    color_orange_border = pygame.draw.rect(sc, GRAY, (295, 105, 60, 60), 5)
    color_orange = pygame.draw.rect(sc, ORANGE, (300, 110, 50, 50))
    color_pink_border = pygame.draw.rect(sc, GRAY, (375, 105, 60, 60), 5)
    color_pink = pygame.draw.rect(sc, PINK, (380, 110, 50, 50))
    color_purple_border = pygame.draw.rect(sc, GRAY, (455, 105, 60, 60), 5)
    color_purple = pygame.draw.rect(sc, PURPLE, (460, 110, 50, 50))
    color_black_border = pygame.draw.rect(sc, GRAY, (535, 105, 60, 60), 5)
    color_black = pygame.draw.rect(sc, BLACK, (540, 110, 50, 50))

    # Draw tool selection buttons
    brush_button = pygame.draw.rect(sc, GRAY, (660, 30, 60, 60), 5)
    pygame.draw.line(sc, BLACK, (665, 60), (715, 60), 4)

    square_button = pygame.draw.rect(sc, GRAY, (660, 110, 60, 60), 5)
    pygame.draw.rect(sc, current_color, (665, 115, 50, 50))

    circle_button = pygame.draw.rect(sc, GRAY, (735, 110, 60, 60), 5)
    pygame.draw.circle(sc, current_color, (765, 140), 25)

    rhombus_button = pygame.draw.rect(sc, GRAY, (810, 110, 55, 55), 5)
    pygame.draw.polygon(sc, current_color, ((837.5, 115), (860, 137.5), (837.5, 160), (815, 137.5)))

    right_tr_button = pygame.draw.rect(sc, GRAY, (735, 30, 60, 60), 5)
    pygame.draw.polygon(sc, current_color, ((745, 35), (745, 85), (785, 85)))

    eq_tr_button = pygame.draw.rect(sc, GRAY, (810, 30, 60, 60), 5)
    pygame.draw.polygon(sc, current_color, ((837.5, 35), (865, 85), (815, 85)))

    # Draw UI section lines
    pygame.draw.line(sc, BLACK, (0, 180), (900, 180), 3)
    pygame.draw.line(sc, BLACK, (270, 180), (270, 0), 3)
    pygame.draw.line(sc, BLACK, (630, 180), (630, 0), 3)

    # Add section labels
    write_color = font.render("Colors", True, BLACK)
    write_current = font.render("Now using", True, BLACK)
    write_tools = font.render("Tools", True, BLACK)

    sc.blit(write_current, (60, 10))
    sc.blit(write_color, (420, 10))
    sc.blit(write_tools, (660, 10))
    sc.blit(eraser, eraser_rect)

    # Update display and control frame rate
    pygame.display.update()
    clock.tick(60)

import pygame

pygame.init()

W, H = 800, 800
sc = pygame.display.set_mode((W, H))

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
colors = {'white': (255, 255, 255), 'black': (0, 0, 0), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'orange': (252, 154, 8), 'yellow': (252, 248, 3), 'pink': (252, 3, 252), 'purple': (169, 3, 252), 'gray': (206, 204, 207)}

eraser = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab_8\eraser.png").convert_alpha()
eraser = pygame.transform.scale(eraser, (eraser.get_width()//15, eraser.get_height()//15))
eraser_rect = eraser.get_rect(center=(700, 70))
eraser2 = eraser
eraser2 = pygame.transform.scale(eraser2, (eraser2.get_width()//1.5, eraser2.get_height()//1.5))
current_color = RED
current_figure = "rect"

drawed = []

sc.fill(WHITE)

x, y = 0, 0

clock = pygame.time.Clock()

font = pygame.font.Font(r"C:\Users\user\Desktop\PP2\Lab_8\font_user.ttf", 15)

'''def borders(current_color, sc):
    global colors
    for i in colors:
        if i.key == current_color:
            pygame.rect
    
    pygame.draw.rect()'''




sp = None

current_draws = []
draw_area = pygame.Surface((800, 617))
draw_area_rect = draw_area.get_rect(topleft=(0, 183))
is_drawing = False
is_erase = False
is_visible = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
            elif eraser_rect.collidepoint(event.pos):
                is_visible = not is_visible
                is_erase = not is_erase
            
                
    sc.fill(WHITE)  
    
    #draw_area.fill(WHITE) 
    #sc.blit(draw_area, (0, 183))
    pressed = pygame.mouse.get_pressed()
    if pressed[0] and pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<=800 and pygame.mouse.get_pos()[1]>=183 and pygame.mouse.get_pos()[1]<=800: 
        drawed.append((pygame.mouse.get_pos(), current_color))
    
    
    pygame.mouse.set_visible(is_visible)
    
    

    for i in drawed:
        pygame.draw.circle(sc, i[1], i[0], 5)
    
    if is_erase:
        sc.blit(eraser2, pygame.mouse.get_pos())
        pressed2 = pygame.mouse.get_pressed()
        if pressed2[0]:
            mx, my = pygame.mouse.get_pos()
            new_drawed = []
            for pos, color in drawed:
                dx = pos[0] - mx
                dy = pos[1] - my
                distance = (dx**2 + dy**2)**0.5
                if distance > 10:  
                    new_drawed.append((pos, color))
            drawed = new_drawed
        
        
        
    pygame.draw.rect(sc, GRAY, (50, 30, 130, 130), 5)
    pygame.draw.rect(sc, current_color, (55, 35, 120, 120))
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

    pygame.draw.line(sc, BLACK, (0, 180), (800, 180), 3)
    pygame.draw.line(sc, BLACK, (270, 180), (270, 0), 3)
    pygame.draw.line(sc, BLACK, (630, 180), (630, 0), 3)

    write_color = font.render("Colors", True, BLACK)
    write_current = font.render("Now using", True, BLACK)
    write_tools = font.render("Tools", True, BLACK)

    sc.blit(write_current, (60, 10))
    sc.blit(write_color, (420, 10))
    sc.blit(write_tools, (660, 10))
    
    sc.blit(eraser, eraser_rect)
    
                
    
    pygame.display.update()
    clock.tick(60)
                                
            


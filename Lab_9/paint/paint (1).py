import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

selected_tool = "diamond"
drawing = False
start_pos = None
drawn_diamonds = []

def draw_diamond(surface, start, end, color=(0, 0, 0), width=2):
    x1, y1 = start
    x2, y2 = end
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    top = (center_x, y1)
    right = (x2, center_y)
    bottom = (center_x, y2)
    left = (x1, center_y)
    pygame.draw.polygon(surface, color, [top, right, bottom, left], width)

running = True
while running:
    screen.fill((255, 255, 255))

    # Отрисовываем все сохранённые ромбы
    for diamond in drawn_diamonds:
        draw_diamond(screen, diamond[0], diamond[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and selected_tool == "diamond":
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and selected_tool == "diamond":
            drawing = False
            end_pos = event.pos
            drawn_diamonds.append((start_pos, end_pos))  # Сохраняем координаты

    # Если зажата мышь — рисуем временный ромб
    if drawing and selected_tool == "diamond":
        current_pos = pygame.mouse.get_pos()
        draw_diamond(screen, start_pos, current_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

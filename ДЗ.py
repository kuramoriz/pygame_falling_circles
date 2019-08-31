import pygame
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return pygame.Color(r, g, b)


pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
fps = 50
v = 100
circle_radius = 10
running = True

circles = []
circles_colors = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            circles.append(event.pos)
            circles_colors.append(random_color())

    screen.fill((0, 0, 0))
    screen.blit(screen2, (0, 0))
    for i in range(len(circles)):
        circle = circles[i]
        color = circles_colors[i]
        pygame.draw.circle(screen, color, circle, circle_radius)
        new_y = min(circle[1] + v / fps, height - circle_radius)
        circles[i] = (circles[i][0], int(new_y))

    if circles:
        circle = circles[0]
        color = circles_colors[0]
        if circle[1] == height - circle_radius:
            pygame.draw.circle(screen2, color, circle, circle_radius)
            circles.pop(0)
            circles_colors.pop(0)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

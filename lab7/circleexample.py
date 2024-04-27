import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)  

BALL_RADIUS = 25
ball_x = (WIDTH - BALL_RADIUS * 2) // 2
ball_y = (HEIGHT - BALL_RADIUS * 2) // 2
ball_speed = 5  # Уменьшим скорость для более управляемого движения

ball_color = RED  

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), BALL_RADIUS)

    keys = pygame.key.get_pressed()  # Получаем список всех нажатых клавиш

    if keys[pygame.K_UP]:
        if ball_y - ball_speed >= 0:
            ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        if ball_y + ball_speed <= HEIGHT - BALL_RADIUS * 2:
            ball_y += ball_speed
    if keys[pygame.K_LEFT]:
        if ball_x - ball_speed >= 0:
            ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        if ball_x + ball_speed <= WIDTH - BALL_RADIUS * 2:
            ball_x += ball_speed

    
    if ball_x <= 0 or ball_x >= WIDTH - BALL_RADIUS * 2 or ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS * 2:
        ball_color = GREEN
    else:
        ball_color = RED  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

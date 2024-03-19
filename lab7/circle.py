import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


BALL_RADIUS = 25
ball_x = (WIDTH - BALL_RADIUS * 2) // 2
ball_y = (HEIGHT - BALL_RADIUS * 2) // 2
ball_speed = 20


running = True
while running:
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= HEIGHT - BALL_RADIUS * 2:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= WIDTH - BALL_RADIUS * 2:
                    ball_x += ball_speed

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

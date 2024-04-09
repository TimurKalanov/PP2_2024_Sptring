import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the drawing window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Program")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set default drawing parameters
drawing_color = BLACK
drawing_tool = "pen"
drawing_size = 5
drawing = False

# Function to draw shapes
def draw_shape(shape, start_pos, end_pos):
    if shape == "rectangle":
        pygame.draw.rect(screen, drawing_color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
    elif shape == "circle":
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
        center = (start_pos[0] + radius, start_pos[1] + radius)
        pygame.draw.circle(screen, drawing_color, center, radius)
    elif shape == "eraser":
        pygame.draw.circle(screen, WHITE, end_pos, drawing_size)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                drawing_tool = "rectangle"
            elif event.key == pygame.K_c:
                drawing_tool = "circle"
            elif event.key == pygame.K_e:
                drawing_tool = "eraser"
            elif event.key == pygame.K_UP:
                drawing_size += 1
            elif event.key == pygame.K_DOWN:
                drawing_size -= 1
            elif event.key == pygame.K_SPACE:
                drawing_color = BLACK if drawing_color != BLACK else WHITE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                end_pos = event.pos
                draw_shape(drawing_tool, start_pos, end_pos)
                start_pos = end_pos

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

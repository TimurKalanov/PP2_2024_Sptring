import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collect Coins Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Variables
coin_size = 30
coin_speed = 5
coins_collected = 0

# Function to create a new coin
def create_coin():
    x = random.randint(0, screen_width - coin_size)
    y = -coin_size
    return {'rect': pygame.Rect(x, y, coin_size, coin_size), 'speed': coin_speed}

# Main game loop
running = True
clock = pygame.time.Clock()
coins = []

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new coins randomly
    if random.randint(0, 100) < 5:
        coins.append(create_coin())

    # Move and draw coins
    for coin in coins:
        coin['rect'].move_ip(0, coin['speed'])
        pygame.draw.ellipse(screen, YELLOW, coin['rect'])

    # Remove coins that have gone off screen
    coins = [coin for coin in coins if coin['rect'].top < screen_height]

    # Check for collisions with the player (not implemented here)

    # Show the number of collected coins
    coins_text = font.render(f'Coins: {coins_collected}', True, WHITE)
    screen.blit(coins_text, (screen_width - coins_text.get_width() - 10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

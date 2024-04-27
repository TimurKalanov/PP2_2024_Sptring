# importing libraries
import pygame
import time
import random
import csv
import psycopg2 as pgsql

connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres",
                         password="12345678", port=5432)
cur=connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS snakegame (
    username VARCHAR(255),
    user_score INT,
    user_level INT
);
""")




snake_speed = 15
level = 1  # начальный уровень

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50]
			
			]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
				random.randrange(1, (window_y//10)) * 10]

# defining different weight for the fruit
fruit_weights = {
    'apple': 1,
    'banana': 3,
    'orange': 2
}

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):
	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	# create the display surface object 
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	# displaying text
	game_window.blit(score_surface, score_rect)

# game over function
def game_over():
	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	# creating a text surface on which text 
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	# create a rectangular object for the text 
	# surface object
	game_over_rect = game_over_surface.get_rect()
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	# after 2 seconds we will quit the program
	time.sleep(2)
	# deactivating pygame library
	pygame.quit()
	# quit the program
	quit()

def insert(newuser):
    cur.execute("""INSERT INTO snakegame VALUES ('{}',0,0)""".format(newuser))

def update(curuser):
    cur.execute("SELECT * FROM snakegame WHERE username='{}'".format(curuser))
    data=cur.fetchone()
    cur.execute("""UPDATE snakegame
    SET user_score={}, user_level={}
    WHERE username='{}'
    """.format(max(data[1],CNTSHASHLYK+CNTQAZY*5),max(data[2],1+(CNTSHASHLYK+CNTQAZY)//10),curuser))
    connection.commit()


print("Enter your username:")
user=input()
cur.execute("SELECT count(*) FROM snakegame WHERE username='{}'".format(user))
if cur.fetchone()[0]==0:
    insert(user)
    connection.commit()
else:
    cur.execute("SELECT * FROM snakegame WHERE username='{}'".format(user))
    data=cur.fetchone()
    print("User's max score:{}".format(data[1]))
    print("User's max level:{}".format(data[2]))
welcomescreen=False

print("game will start in:")

for i in range(1,4):
    print(i)
    time.sleep(1)
print("go!")




# Main Function
while True:
	# handling key events
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

	# If two keys pressed simultaneously
	# we don't want snake to move into two 
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by respective weight
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += fruit_weights[random.choice(list(fruit_weights.keys()))] 
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10, 
						random.randrange(1, (window_y//10)) * 10]
		fruit_spawn = True

	# увеличение уровня и скорости
	if score >= 5 * level:  # условие для перехода на следующий уровень
		level += 1
		snake_speed += 5  # увеличение скорости
		# здесь вы можете добавить другие действия при переходе на следующий уровень

	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, red,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score continuously
	show_score(1, white, 'times new roman', 20)

	# отображение уровня
	show_score(1, white, 'times new roman', 20)

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)

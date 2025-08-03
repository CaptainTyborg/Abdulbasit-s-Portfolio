import pygame
import time
import random

pygame.init()

# Display dimensions
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Clock and fonts
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 25)
score_font = pygame.font.SysFont("comicsans", 30)

# Snake block size and speed
block_size = 10
speed = 10

def draw_snake(block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(win, black, [segment[0], segment[1], block, block])

def show_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    win.blit(value, [10, 10])

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(white)
            message("You Lost! Press C-Continue or Q-Quit", red)
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x_change == 0:  # Prevent 180-turn
                        x_change = -block_size
                        y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x_change == 0:
                        x_change = block_size
                        y_change = 0
                elif event.key == pygame.K_UP:
                    if y_change == 0:
                        y_change = -block_size
                        x_change = 0
                elif event.key == pygame.K_DOWN:
                    if y_change == 0:
                        y_change = block_size
                        x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(blue)
        pygame.draw.rect(win, green, [food_x, food_y, block_size, block_size])

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == head:
                game_close = True

        draw_snake(block_size, snake)
        show_score(length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()

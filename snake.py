import random
import pygame
import sys

display_width = 640
display_height = 480
cell_size = 20
block_width = int(display_width / cell_size)
block_height = int(display_height / cell_size)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (0, 155, 0)
BG_COLOR = (255, 255, 255)

UP, DOWN = 'up', 'down'
LEFT, RIGHT = 'left', 'right'
fps_lock = pygame.time.Clock()
display = pygame.display.set_mode((display_width, display_height))


def run_game():
    start_x = random.randint(5, block_width - 6)
    start_y = random.randint(5, block_height - 6)
    snake = [[start_x, start_y],
             [start_x - 1, start_y],
             [start_x - 2, start_y]]
    snake_head = [snake[0][0] + 1, snake[0][1]]

    direction = RIGHT
    apple = apple_spawn()
    while True:
        display.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a) and direction != RIGHT:
                    direction = LEFT
                if (event.key == pygame.K_d) and direction != LEFT:
                    direction = RIGHT
                if (event.key == pygame.K_w) and direction != DOWN:
                    direction = UP
                if (event.key == pygame.K_s) and direction != UP:
                    direction = DOWN
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        for coord in snake[1:]:
            if coord == snake[0]:
                run_game()

        if snake[0][0] == block_width + 1 or snake[0][0] == -1:
            snake[0][0] = block_width - snake[0][0]
        if snake[0][1] == block_height + 1 or snake[0][1] == -1:
            snake[0][1] = block_height - snake[0][1]

        if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
            snake.append([])
            apple = apple_spawn()
        if direction == UP:
            snake_head = [snake[0][0], snake[0][1] - 1]
        if direction == DOWN:
            snake_head = [snake[0][0], snake[0][1] + 1]
        if direction == LEFT:
            snake_head = [snake[0][0] - 1, snake[0][1]]
        if direction == RIGHT:
            snake_head = [snake[0][0] + 1, snake[0][1]]

        del snake[-1]
        snake.insert(0, snake_head)
        draw_apple(apple)
        draw_snake(snake)
        pygame.display.update()
        fps_lock.tick(5)


def apple_spawn():
    return [random.randint(0, block_width - 1), random.randint(0, block_height - 1)]


def draw_snake(snake):
    for coord in snake:
        x = coord[0] * cell_size
        y = coord[1] * cell_size
        snake_rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(display, YELLOW, snake_rect)
        rect_in_worm = pygame.Rect(x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(display, GREEN, rect_in_worm)


def draw_apple(apple):
    x = cell_size * apple[0]
    y = cell_size * apple[1]
    apple = pygame.Rect(x, y, cell_size, cell_size)
    pygame.draw.rect(display, RED, apple)


run_game()

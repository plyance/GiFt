import pygame
import random
import time

# 初始化pygame
pygame.init()

# 设置游戏窗口大小
window_width = 800
window_height = 600

# 蛇的大小和速度
snake_block = 20
snake_speed = 15

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇小游戏")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, WHITE, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

# 初始化游戏
game_over = False
game_close = False

x1 = window_width / 2
y1 = window_height / 2

snake_block_size = snake_block
snake_list = []
length_of_snake = 1

food_x = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
food_y = round(random.randrange(0, window_height - snake_block) / snake_block) * snake_block

x1_change = 0
y1_change = 0

# 游戏循环
while not game_over:
    while game_close:
        window.fill(BLACK)
        message("你输了！按Q退出，按C重新开始", RED)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_over = False
                    game_close = False
                    x1 = window_width / 2
                    y1 = window_height / 2
                    snake_list = []
                    length_of_snake = 1
                    food_x = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
                    food_y = round(random.randrange(0, window_height - snake_block) / snake_block) * snake_block
                    x1_change = 0
                    y1_change = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_close = True

    x1 += x1_change
    y1 += y1_change
    window.fill(BLACK)
    pygame.draw.rect(window, RED, [food_x, food_y, snake_block, snake_block])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_Head:
            game_close = True

    our_snake(snake_block, snake_list)
    pygame.display.update()

    if x1 == food_x and y1 == food_y:
        length_of_snake += 1
        food_x = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, window_height - snake_block) / snake_block) * snake_block

    clock.tick(snake_speed)

pygame.quit()
quit()
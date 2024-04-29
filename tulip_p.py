import numpy as np
import pygame
import sys
from pygame.locals import *

pygame.init()

# 画面のサイズと色の設定
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ウィンドウの作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rectangle Animation')

# 長方形の初期設定
# rect_width, rect_height = 20, 100
# rect_color = BLACK
# rect_center = (WIDTH // 2, HEIGHT // 2)
# rotation_angle = 0

def rotated(degree):
    theta = np.deg2rad(degree)
    return np.array(
            [[np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]]
        )

degree = 0
start_pos = (WIDTH // 2, HEIGHT // 2)
start_vec = np.array([0, 100])

clock = pygame.time.Clock()
open_flag = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)

    if open_flag:
        degree += 10
    else:
        degree -= 10

    a = rotated(degree)
    vec = np.dot(a, start_vec)
    end_pos = start_pos[0] + vec[0], start_pos[1] - vec[1]

    pygame.draw.line(screen, BLACK, start_pos, end_pos, 2)

    if degree == 90:
        open_flag = False
    if degree == 0:
        open_flag = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
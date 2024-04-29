import math
import pygame
from pygame.locals import *
import sys

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((20, 20))
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,0,0), (20, 20), 20)
        # self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (800 // 2, 600 - 50)
        self.speed = 5

        degrees = 10
        radians = math.radians(degrees)
        self.speed_x = self.speed / math.cos(radians)  # 水平方向の速度
        self.speed_y = -self.speed / math.sin(radians)  # 垂直方向の速度


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.bottom < 0:
            self.kill()

        # 画面の境界に達したときに速度を反転させる
        if self.rect.top <= 0:
            self.speed_y *= -1

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    RED = (255,0,0)
    BALL_SIZE = 20
    BALL_SPEED = 5

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ball_group = pygame.sprite.Group()

    shooting = False
    last_shot_time = 0
    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shooting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shooting = False
        
        # if shooting and current_time - last_shot_time > 1000:  # 1秒ごとに発射
        if shooting and current_time - last_shot_time > 500:  # 0.5秒ごとに
            ball = Ball()
            ball_group.add(ball)

            last_shot_time = current_time

        screen.fill((0,0,0))
        ball_group.update()
        ball_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    # ball_x = WIDTH // 4
    # ball_y = HEIGHT - BALL_SIZE / 2
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # while True:
    #     screen.fill((0,0,0))
    #     pygame.draw.circle(screen,RED,(ball_x,ball_y),BALL_SIZE)

    #     pygame.display.update()

    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()

if __name__ == "__main__":
    main()
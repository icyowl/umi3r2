import math
import numpy as np
import pygame
from pygame.locals import *
import sys


WIDTH, HEIGHT = 800, 600

class Tulip:
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.start_pos = WIDTH // 2, HEIGHT // 2
        self.start_vec = 0, 100
        self.open_flag = True
        self.degree = 0

    @staticmethod
    def rotated(degree: int) -> np.ndarray:
        theta = np.deg2rad(degree)
        return np.array(
                [[np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]]
            )

    def petal(self, sign=1):
        # sign=1 is left, sign=-1 is right
        if self.open_flag:
            self.degree += sign * 1
        else:
            self.degree += sign * -1

        a = self.rotated(self.degree)
        vec = np.dot(a, self.start_vec)
        end_pos = self.start_pos[0] + vec[0], self.start_pos[1] - vec[1]
        pygame.draw.line(self.screen, (255, 255, 255), self.start_pos, end_pos, 2)

        if self.degree == sign * 60:
            self.open_flag = False
        if self.degree == 0:
            self.open_flag = True


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    left_ = Tulip(screen)
    right_ = Tulip(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0,0,0))
        
        left_.petal(sign=1)
        right_.petal(sign=-1)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
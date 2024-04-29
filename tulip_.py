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
        self.right_flag = True
        self.right_degree = 0
        self.left_flag = True
        self.left_degree = 0

    @staticmethod
    def rotated(right_degree):
        theta = np.deg2rad(right_degree)
        return np.array(
                [[np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]]
            )

    def right_petal(self):
        if self.right_flag:
            self.right_degree += 1
        else:
            self.right_degree -= 1

        a = self.rotated(self.right_degree)
        vec = np.dot(a, self.start_vec)
        end_pos = self.start_pos[0] + vec[0], self.start_pos[1] - vec[1]
        pygame.draw.line(self.screen, (255, 255, 255), self.start_pos, end_pos, 2)

        if self.right_degree == 60:
            self.right_flag = False
        if self.right_degree == 0:
            self.right_flag = True

    def left_petal(self):
        if self.left_flag:
            self.left_degree -= 1
        else:
            self.left_degree += 1

        a = self.rotated(self.left_degree)
        vec = np.dot(a, self.start_vec)
        end_pos = self.start_pos[0] + vec[0], self.start_pos[1] - vec[1]
        pygame.draw.line(self.screen, (255, 255, 255), self.start_pos, end_pos, 2)

        if self.left_degree == -60:
            self.left_flag = False
        if self.left_degree == 0:
            self.left_flag = True


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    spam = Tulip(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0,0,0))
        
        spam.right_petal()
        spam.left_petal()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
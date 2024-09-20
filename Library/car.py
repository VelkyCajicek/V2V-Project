import pygame
import math

class Car():
    def __init__(self, screen_size : int, screen : pygame.Surface, block_size : int, grid_map : list) -> None:
        self.screen = screen
        self.block_size = block_size
        self.grid_map = grid_map
        self.width = self.block_size / 2
        self.height = self.block_size / 3
        self.speed = 2
        self.x_pos = 0
        self.y_pos = screen_size / 2 - 30

    def move(self):
        self.x_pos += self.speed
        pygame.draw.rect(self.screen, (128, 255, 0), pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))
        pygame.display.flip()
        self.check_for_intersection()

    def check_for_intersection(self):
        pass
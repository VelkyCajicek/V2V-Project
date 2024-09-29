import pygame

class Road():
    def __init__(self, screen : pygame.Surface, block_size : int, position : tuple) -> None:
        self.screen = screen
        self.block_size = block_size
        self.position = position
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.position))

class Dashed(Road):
    def __init__(self, screen, block_size, position) -> None:
        super().__init__(screen, block_size, position)
        self.dash_position = (self.position[0] + block_size / 5 * 2, self.position[1] + block_size / 5 + 10, 16, 4)
        #pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.dash_position))
        
            
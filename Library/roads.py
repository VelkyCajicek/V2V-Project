import pygame

class Road():
    def __init__(self, screen : pygame.Surface, section_size : list, position : tuple) -> None:
        self.screen = screen
        self.section_size = section_size
        self.position = position
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.position))
     
class Dashed(Road):
    def __init__(self, screen, section_size, position) -> None:
        super().__init__(screen, section_size, position)
        self.dash_position = (self.position[0] / 2 - self.position[0] * 0.1, self.position[1] / 2 + self.position[1] * 0.1, self.position[2] / 2 + self.position[2] * 0.1, self.position[3] / 2 - self.position[3] * 0.1)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.dash_position))
        
            
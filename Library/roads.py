import pygame

class Road():
    def __init__(self, screen : pygame.Surface, block_size : int, position : tuple) -> None:
        self.screen = screen
        self.block_size = block_size
        self.position = position
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.position))
    
    #def neighbors(radius, row_number, column_number):
    #    return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
    #        for j in range(column_number-1-radius, column_number+radius)]
    #            for i in range(row_number-1-radius, row_number+radius)]
     
class Dashed(Road):
    def __init__(self, screen, block_size, position) -> None:
        super().__init__(screen, block_size, position)
        self.dash_position = (self.position[0] + block_size / 5 * 2, self.position[1] + block_size / 5 + 10, 16, 4)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.dash_position))
        
            
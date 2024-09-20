import pygame
import map_generation as mg
import roads as rd
from pre_defined_maps import cross_map
from car import Car

pygame.init()

class GUI():
    def __init__(self, screen_size : int, grid_array_size : int) -> None: # Assuming the screen is square
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode([screen_size, screen_size])
        self.grid_map = cross_map #mg.Map_Generation(grid_array_size).grid
        self.block_size = self.screen_size / len(self.grid_map)
        self.mainLoop()
    
    def generate_map(self) -> None:
        for i in range(0, len(self.grid_map)):
            for j in range(0, len(self.grid_map[i])):
                if(self.grid_map[i][j] == 1):
                    rd.Dashed(self.screen, self.block_size, (j*self.block_size, i*self.block_size, self.block_size, self.block_size))  # First two start position and then size

    def mainLoop(self) -> None:        
        clock = pygame.time.Clock()
        
        
        pygame.display.flip()
        
        test_car = Car(self.screen_size, self.screen, self.block_size)

        running = True
        while running: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 178, 102)) # Color of the background
            self.generate_map()
            test_car.move()

            clock.tick(60)
        pygame.quit()
        
if __name__ == "__main__":
    gui = GUI(500, 10)
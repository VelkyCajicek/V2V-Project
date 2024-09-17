import pygame
import map_generation as mg
import roads as rd

class GUI():
    def __init__(self, screen_size : int, grid_array_size : int) -> None: # Assuming the screen is square
        self.screen_size = screen_size
        self.grid_array_size = grid_array_size
        self.screen = pygame.display.set_mode([screen_size, screen_size])
        self.grid_map = mg.Map_Generation(self.grid_array_size).grid
        self.mainLoop()
    
    def generate_map(self):
        block_size = self.screen_size / self.grid_array_size
        print(block_size)
        for j in range(0, self.grid_array_size):
            i = 0
            rd.Dashed(self.screen, [block_size / 2, block_size / 2], (j*block_size, i*block_size, (j+1)*block_size, (i+1)*block_size)) 

    
    def mainLoop(self) -> None:        
        self.screen.fill((255, 255, 255)) # Color of the background
        self.generate_map()
        pygame.display.flip()
       
        self.DisplayList(self.grid_map)
        
        running = True
        while running: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()
        
    def DisplayList(self, array):
        for row in array:
            print(row)
        

if __name__ == "__main__":
    gui = GUI(500, 10)
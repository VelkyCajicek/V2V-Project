import numpy as np
import random

class Map_Generation():
    def __init__(self, grid_size : int) -> None:
        self.grid_size = grid_size
        self.grid = self.generate_path()
    
    def is_valid_move(self, new_x, new_y, grid, directions):
            # Check if the move is within bounds
            if not (0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size):
                return False

            # Check if the move would create multiple adjacent ones
            adjacent_counts = sum(grid[new_x + dx, new_y + dy] == 1 for dx, dy in directions if 0 <= new_x + dx < self.grid_size and 0 <= new_y + dy < self.grid_size)

            return grid[new_x, new_y] == 0 and adjacent_counts < 2
    
    def generate_path(self):
        grid = np.zeros((self.grid_size, self.grid_size), dtype=int) # Have to include dtype here
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Define the directions for movement (right, down, left, up)
        start_pos = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        
        x, y = start_pos
        grid[x, y] = 1  # Mark the starting point
        path = [(x, y)] # Initialize the path with the starting point

        while path:
            x, y = path[-1]

            # Get possible directions
            possible_directions = [(x + dx, y + dy) for dx, dy in directions]
            valid_moves = [pos for pos in possible_directions if self.is_valid_move(pos[0], pos[1], grid, directions)]

            if valid_moves:
                # Choose a random valid move
                next_pos = random.choice(valid_moves)
                grid[next_pos[0], next_pos[1]] = 1 
                path.append(next_pos)  
            else:
                # No valid moves
                path.pop()
        
        return grid.tolist()

if __name__ == "__main__":
    grid = Map_Generation(10).generate_path()
    print(grid)
import pygame
import math
import random

class Car():
    def __init__(self, screen_size : int, screen : pygame.Surface, block_size : int) -> None:
        self.screen = screen
        self.block_size = block_size
        self.width = self.block_size / 2
        self.length = self.block_size / 3
        self.speed = 2
        self.x_pos = 0
        self.y_pos = screen_size / 2 - 30

    def move(self):
        car_body = pygame.draw.rect(self.screen, (128, 255, 0), pygame.Rect(self.x_pos, self.y_pos, self.width, self.length))
        # Sensors around veichle
        # Positions of sensors (front, right, left)
        sensor_positions = [((self.x_pos + self.width + self.block_size / 2), self.y_pos + self.length / 2), (self.x_pos + self.width / 2, self.y_pos + self.length + self.block_size / 2), (self.x_pos + self.width / 2, self.y_pos + self.length - self.block_size)]
        # * before argument unpacks tuple 
        front_sensor = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(*sensor_positions[0], self.width / 10, self.length / 10))
        right_sensor = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(*sensor_positions[1], self.width / 10, self.length / 10))
        left_sensor = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(*sensor_positions[2], self.width / 10, self.length / 10))
        pygame.display.flip()
        self.check_for_intersection(sensor_positions)


    def check_for_intersection(self, sensor_positions):
        valid_directions = []
        self.x_pos += self.speed
        direction = 0
        
        for i in range(0, len(sensor_positions) - 1):
            x,y = sensor_positions[i]
            if(self.screen.get_at((math.floor(x) + 1, math.floor(y) + 1)) == (0, 0, 0)):
                valid_directions.append(i)
        if(len(valid_directions) > 1):
            direction = valid_directions[random.randint(0, len(valid_directions) - 1)]
        
        match direction: # 0 = Straight, 1 = Right, 2 = Left, 3 = Back
            case 0: 
                self.x_pos += self.speed  
            case 1:
                self.y_pos += self.speed
            case 2:
                self.y_pos -= self.speed 
            case 3: 
                self.y_pos -= self.speed 
    
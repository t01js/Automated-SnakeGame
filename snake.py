import pygame
import sys
import random

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)

    def move_towards_food(self, food_position):
        head_x, head_y = self.body[0]
        food_x, food_y = food_position

        possible_directions = []

        if head_x < food_x and self.direction != (-10, 0):
            possible_directions.append((10, 0))
        elif head_x > food_x and self.direction != (10, 0):
            possible_directions.append((-10, 0))

        if head_y < food_y and self.direction != (0, -10):
            possible_directions.append((0, 10))
        elif head_y > food_y and self.direction != (0, 10):
            possible_directions.append((0, -10))

        if possible_directions:
            self.direction = random.choice(possible_directions)

    def update(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, position):
        return self.body[0] == position

    def check_wall_collision(self):
        head = self.body[0]
        return head[0] < 0 or head[0] >= 640 or head[1] < 0 or head[1] >= 480

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 10, 10))

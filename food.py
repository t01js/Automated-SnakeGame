import pygame
import sys
import random

class Food:
    def __init__(self):
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, 63) * 10, random.randint(0, 47) * 10)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], 10, 10))

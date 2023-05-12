import pygame
import sys
import random

from snake import Snake
from food import Food

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while True:
            self.handle_events()
            if not self.update():
                break
            self.draw()
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.snake.move_towards_food(self.food.position)
        self.snake.update()
        if self.snake.check_collision(self.food.position):
            self.snake.grow()
            self.food.randomize_position()
            self.score += 1
        elif self.snake.check_wall_collision() or self.snake.check_self_collision():
            return False
        return True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

if __name__ == "__main__":
    game = Main()
    game.run()

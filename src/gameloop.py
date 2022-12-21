import sys
import pygame
from snake import Snake
from food import Food
from death import Death
from score import Score
from keyboard_events import KeyboardEvents

class GameLoop():
    """Class that has the game's main loop."""
    def __init__(self):
        """Class constructor, creates variables, calls other classes."""
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.death  = Death(self.snake, self.score)
        self.screen_proportions = (640, 480)
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((self.screen_proportions[0], self.screen_proportions[1]))
        self.events = KeyboardEvents()

    def keyboard(self):
        for event in self.events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.turn_up()
                if event.key == pygame.K_DOWN:
                    self.snake.turn_down()
                if event.key == pygame.K_LEFT:
                    self.snake.turn_left()
                if event.key == pygame.K_RIGHT:
                    self.snake.turn_right()
            if event.type == pygame.QUIT:
                sys.exit()

    def main(self):
        """Main loop."""
        pygame.init()
        #screen = pygame.display.set_mode((self.screen_proportions[0], self.screen_proportions[1]))
        clock = pygame.time.Clock()

        while True:
            if self.snake.dead:
                self.death.die()
            if self.death.call_main:
                self.death.call_main = False
                self.main()
            self.keyboard()
            self.screen.fill((255, 248, 220))
            self.snake.move()
            self.snake.draw_snake(self.screen)
            self.food.draw_food(self.screen)
            self.score.eating(self.snake, self.food)
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    GameLoop().main()

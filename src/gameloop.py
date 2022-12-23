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
        pygame.display.set_caption("Snake")
        self.screen_size = (640, 480)
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.snake = Snake(self.screen_size)
        self.food = Food()
        self.score = Score()
        self.death  = Death(self.snake, self.score, self.screen_size)
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
        clock = pygame.time.Clock()

        while True:
            if self.snake.dead:
                self.death.die()
                while True:
                    self.death.gameover_loop()
                    if self.death.call_main:
                        self.death.reset()
                        break
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

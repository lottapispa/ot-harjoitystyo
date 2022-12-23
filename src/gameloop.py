import pygame
from snake import Snake
from food import Food
from death import Death
from score import Score
from keyboard_events import KeyboardEvents
from keyboard import KeyBoard

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
        self.keyboard = KeyBoard(self.snake, self.screen_size, self.events)

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
            self.keyboard.keyboard()
            self.screen.fill((255, 248, 220))
            self.snake.move()
            self.snake.draw_snake(self.screen)
            self.food.draw_food(self.screen)
            self.score.eating(self.snake, self.food)
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    GameLoop().main()

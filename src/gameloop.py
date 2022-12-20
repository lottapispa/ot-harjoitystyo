import sys
import pygame
from snake import Snake
from food import Food
from keyboard_events import KeyboardEvents

class GameLoop():
    """Class that has the game's main loop."""
    def __init__(self):
        """Class constructor, creates variables, calls other classes."""
        self.snake = Snake()
        self.food = Food()
        self.screen_width = 640
        self.screen_height = 480
        pygame.display.set_caption("Snake")
        self.events = KeyboardEvents()
        self.font = pygame.font.SysFont("Candara", 24)
        self.bigfont = pygame.font.SysFont("Candara", 36)

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

    def die(self):
        """Game over window."""
        pygame.init()
        self.snake.die_called = True
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen.fill((255, 248, 220))
        pygame.draw.rect(screen, (0, 0, 0), (220, 100, 200, 290))

        #texts and blitting them
        game_over = self.bigfont.render("Game Over", True, (255, 97, 3))
        screen.blit(game_over, (250, 130))

        points = self.font.render(f"Points: {self.snake.points}", True, (255, 248, 220))
        screen.blit(points, (275, 175))

        time = self.font.render("Time: ", True, (255, 248, 220))
        screen.blit(time, (275, 215))

        highscore = self.font.render(f"Highscore: {self.snake.highscore}", True, (255, 248, 220))
        screen.blit(highscore, (275, 255))

        play_again = self.font.render("Play Again", True, (255, 248, 220))
        screen.blit(play_again, (275, 295))

        quit_game = self.font.render("Quit Game", True, (255, 248, 220))
        screen.blit(quit_game, (275, 335))

        pygame.display.flip()
        while True:
            self.gameover_loop()

    def gameover_loop(self):
        """Game over window's while loop's content.
        Makes buttons in gameover window work."""
        for event in self.events.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 275 <= mouse[0] <= 355 and 295 <= mouse[1] <= 320:
                    self.snake.reset()
                    self.snake.reset_called  = False
                    self.main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 275 <= mouse[0] <= 355 and 335 <= mouse[1] <= 360:
                    sys.exit()

    def main(self):
        """Main loop."""
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        clock = pygame.time.Clock()

        while True:
            if self.snake.dead:
                self.die()
            self.keyboard()
            screen.fill((255, 248, 220))
            self.snake.move()
            self.snake.draw_snake(screen)
            self.food.draw_food(screen)
            self.food.eating(self.snake)
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    GameLoop().main()

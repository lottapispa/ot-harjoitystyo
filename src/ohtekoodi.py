import random
import sys
import pygame
from keyboard_events import KeyboardEvents

class Snake():
    """Class that creates and keeps track of snake."""
    def __init__(self):
        """Class constructor, creates variables."""
        pygame.init()
        self.length = 1
        self.color = (102, 205, 0)
        self.screen_width = 640
        self.screen_height = 480
        self.location = [((self.screen_width/2), (self.screen_height/2))]
        self.up = (0, -1)
        self.down = (0, 1)
        self.left = (-1, 0)
        self.right = (1, 0)
        self.direction = random.choice([self.up,self.down,self.left,self.right])
        self.points = 0
        self.highscore = 0
        self.font = pygame.font.SysFont("Candara", 24)
        self.bigfont = pygame.font.SysFont("Candara", 36)
        self.step = 20 # how much snake moves at once
        self.duration = 0 # tracks how long the game lasts (not used yet)
        self.events = KeyboardEvents()

    def head_location(self):
        """Returns: location of snake's head"""
        return self.location[0]

    def head_rect(self):
        """Returns: snake's head rectangle"""
        self.head = self.location[0]
        self.rect = pygame.Rect((self.head[0], self.head[1]), (20, 20))
        return self.rect

    def draw_snake(self, screen):
        """Draws snake  by drawing a rectangle in every location in list.
        Snake head has a black outline."""
        self.counter = 0
        for location in self.location:
            if self.counter == 0:
                pygame.draw.rect(screen, self.color, pygame.Rect((location[0], location[1]), (20, 20)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((location[0], location[1]), (20, 20)), 1)
            else:
                pygame.draw.rect(screen, self.color, pygame.Rect((location[0], location[1]), (20, 20)))
            self.counter += 1

    """These functions are called by the keyboard function and they change the direction variable."""
    def turn_up(self):
        if self.direction != self.down or self.direction != self.up or self.length == 1:
            self.direction = self.up

    def turn_down(self):
        if self.direction != self.up or self.direction != self.down or self.length == 1:
            self.direction = self.down

    def turn_left(self):
        if self.direction != self.right or self.direction != self.left or self.length == 1:
            self.direction = self.left

    def turn_right(self):
        if self.direction != self.left or self.direction != self.right or self.length == 1:
            self.direction = self.right

    def move(self):
        """Moves snake by adding a new location in list and popping the last location."""
        self.current = self.head_location()
        x = self.direction[0]
        y = self.direction[1]
        if self.direction == self.up or self.direction == self.down:
            self.new_head = (self.current[0], self.current[1] + (self.step * y))
        elif self.direction == self.left or self.direction == self.right:
            self.new_head = (self.current[0] + (self.step * x), self.current[1])
        # snake dies if it hits itself or a wall
        if len(self.location) > 2 and self.new_head in self.location[2:]:
            self.die()
        elif self.new_head[0] + 20 > 640 or self.new_head[0] < 0 or self.new_head[1] + 20 > 480 or self.new_head[1] < 0:
            self.die()
        else:
            self.location.insert(0, self.new_head)
            if len(self.location) > self.length:
                self.location.pop()

    def keyboard(self):
        for event in self.events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn_up()
                if event.key == pygame.K_DOWN:
                    self.turn_down()
                if event.key == pygame.K_LEFT:
                    self.turn_left()
                if event.key == pygame.K_RIGHT:
                    self.turn_right()
            if event.type == pygame.QUIT:
                sys.exit()

    def die(self):
        """Game over window."""
        pygame.init()
        self.die_called = True
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen.fill((255, 248, 220))
        pygame.draw.rect(screen, (0, 0, 0),
                         (220, 100, 200, 290))
        game_over = self.bigfont.render("Game Over", True, (255, 97, 3))
        screen.blit(game_over, (250, 130))
        points = self.font.render(f"Points: {self.points}", True, (255, 248, 220))
        screen.blit(points, (275, 175))
        time = self.font.render("Time: ", True, (255, 248, 220))
        screen.blit(time, (275, 215))
        highscore = self.font.render(
            f"Highscore: {self.highscore}", True, (255, 248, 220))
        screen.blit(highscore, (275, 255))
        play_again = self.font.render(
            "Play Again", True, (255, 248, 220))
        screen.blit(play_again, (275, 295))
        quit_game = self.font.render(
            "Quit Game", True, (255, 248, 220))
        screen.blit(quit_game, (275, 335))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 275 <= mouse[0] <= 355 and 295 <= mouse[1] <= 320:
                        self.reset()
                        GameLoop().main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 275 <= mouse[0] <= 355 and 335 <= mouse[1] <= 360:
                        sys.exit()

    def reset(self):
        """Resets values for a new game."""
        self.reset_called = True
        self.length = 1
        self.location = [((self.screen_width/2), (self.screen_height/2))] 
        self.direction = random.choice([self.up, self.down, self.left, self.right])
        self.points = 0
        self.duration = 0

class Food():
    """Class that creates and keeps track of food"""
    def __init__(self):
        """Class constructor, creates variables."""
        self.size = 10 # radius
        self.color = (139,69,19)
        self.location = (0,0) # center point of circle
        self.random_location()

    def random_location(self):
        """Assigns random location for food to pop up in."""
        self.location = (random.randint(10, 640-10), random.randint(10, 480-10))

    def draw_food(self, screen):
        """Draws food."""
        pygame.draw.circle(screen, self.color, self.location, self.size)

    def eating(self, snake):
        """Grows snake and adds points if snake eats food."""
        if pygame.Rect.collidepoint(snake.head_rect(), self.location) == True:
            snake.length += 1
            snake.points += 1
            # highscore doesn't work yet, it resets too
            if snake.points > snake.highscore:
                snake.highscore = snake.points
            self.random_location()

class GameLoop():
    """Class that has the game's main loop."""
    def __init__(self):
        """Class constructor, creates variables, calls other classes."""
        self.snake = Snake()
        self.food = Food()
        self.screen_width = 640
        self.screen_height = 480
        pygame.display.set_caption("Snake")

    def main(self):
        """Main loop."""
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        clock = pygame.time.Clock()
        while True:
            self.snake.keyboard()
            screen.fill((255, 248, 220)) 
            self.snake.move()
            self.snake.draw_snake(screen)
            self.food.draw_food(screen)
            self.food.eating(self.snake)
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    GameLoop().main()
import random
import sys
import pygame

# Global variables
screen_width = 640
screen_height = 480
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
step = 20 # how much snake moves at once
pygame.display.set_caption("Snake")

class Snake():
    def __init__(self):
        self.length = 1
        self.color = (102, 205, 0)
        self.location = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up,down,left,right])
        self.points = 0
        self.highscore = 0
        self.font = pygame.font.SysFont("Candara", 24)
        self.bigfont = pygame.font.SysFont("Candara", 36)
        self.duration = 0 # how long the game lasts (not used yet)

    def head_location(self):
        return self.location[0]

    def head_rect(self):
        self.head = self.location[0]
        self.rect = pygame.Rect((self.head[0], self.head[1]), (20, 20))
        return self.rect

    def draw_snake(self, screen):
        self.counter = 0
        for location in self.location:
            if self.counter == 0:
                pygame.draw.rect(screen, self.color, pygame.Rect((location[0], location[1]), (20, 20)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((location[0], location[1]), (20, 20)), 1)
            else:
                pygame.draw.rect(screen, self.color, pygame.Rect((location[0], location[1]), (20, 20)))
            self.counter += 1

    def turn_up(self):
        if self.direction != down or self.direction != up or self.length == 1:
            self.direction = up

    def turn_down(self):
        if self.direction != up or self.direction != down or self.length == 1:
            self.direction = down

    def turn_left(self):
        if self.direction != right or self.direction != left or self.length == 1:
            self.direction = left

    def turn_right(self):
        if self.direction != left or self.direction != right or self.length == 1:
            self.direction = right

    def move(self):
        self.current = self.head_location()
        x = self.direction[0]
        y = self.direction[1]
        if self.direction == up or self.direction == down:
            self.new_head = (self.current[0], self.current[1] + (step * y))
        elif self.direction == left or self.direction == right:
            self.new_head = (self.current[0] + (step * x), self.current[1])
        # jos liikkuessa käärmeen pää osuu sen vartaloon tai seinään, se kuolee
        if len(self.location) > 2 and self.new_head in self.location[2:]:
            self.die()
        elif self.new_head[0] + 20 > 640 or self.new_head[0] < 0 or self.new_head[1] + 20 > 480 or self.new_head[1] < 0:
            self.die()
        # lisätään uusi ruutu käärme listaan ja poistetaan lopusta yksi ruutu
        else:
            self.location.insert(0, self.new_head)
            if len(self.location) > self.length:
                self.location.pop()

    def keyboard(self):
        for event in pygame.event.get():
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
        # Game over window
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height))
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
        # jos hiiri painaa nappia, uusi peli
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 275 <= mouse[0] <= 355 and 295 <= mouse[1] <= 320:
                        self.reset()
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 275 <= mouse[0] <= 355 and 335 <= mouse[1] <= 360:
                        sys.exit()

    def reset(self):
        self.length = 1
        self.location = [((screen_width/2), (screen_height/2))] 
        self.direction = random.choice([up, down, left, right])
        self.points = 0
        self.duration = 0

class Food():
    def __init__(self):
        self.size = 10 # radius
        self.color = (139,69,19)
        self.location = (0,0) # center point of circle
        self.random_location()

    def random_location(self):
        self.location = (random.randint(10, 640-10), random.randint(10, 480-10))

    def draw_food(self, screen):
        pygame.draw.circle(screen, self.color, self.location, self.size)

    def eating(self, snake):
        if pygame.Rect.collidepoint(snake.head_rect(), self.location) == True:
            snake.length += 1
            snake.points += 1
            # highscore doesn't work yet, it resets too
            if snake.points > snake.highscore:
                snake.highscore = snake.points
            self.random_location()

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    while True:
        snake.keyboard()
        screen.fill((255, 248, 220)) 
        snake.move()
        snake.draw_snake(screen)
        food.draw_food(screen)
        food.eating(snake)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
import random
import pygame

# Global variables
screenWidth = 640
screenHeight = 480
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((screenWidth, screenHeight))


class Snake():
    def __init__(self):
        self.length = 1
        self.color = (102, 205, 0)  # green
        self.location = [(screenWidth/2), (screenHeight/2)]  # lista
        self.direction = random.choice([up,down,left,right])

    def head_location(self):
        return self.location[0] 

    def draw_snake(self, x, y):
        # 20 is the size of the snake, x & y the location
        pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 20, 20))

    # Jos käärme on vain 1 pituinen, se voi kääntyä mihin tahansa suuntaan. Jos se on isompi niin se voi kääntyä 3 suuntaan
    # eli ei taaksepäin, koska se ei voi mennä itsensä päälle.

    def turn_up(self):
        if self.direction != down or self.length == 1:
            self.direction = up

    def turn_down(self):
        if self.direction != up or self.length == 1:
            self.direction = down

    def turn_left(self):
        if self.direction != right or self.length == 1:
            self.direction = left

    def turn_right(self):
        if self.direction != left or self.length == 1:
            self.direction = right

    def move(self):
        pass
        
    def keyboard(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.turn_up()
                if tapahtuma.key == pygame.K_DOWN:
                    self.turn_down()
                if tapahtuma.key == pygame.K_LEFT:
                    self.turn_left()
                if tapahtuma.key == pygame.K_RIGHT:
                    self.turn_right()
            if tapahtuma.type == pygame.QUIT:
                exit()

    # def grow(self):
    #    pass

    def die(self):
        # Game over window
        pygame.init()
        self.font = pygame.font.SysFont("Candara", 24)
        self.bigfont = pygame.font.SysFont("Candara", 36)
        screen = pygame.display.set_mode((screenWidth, screenHeight))
        screen.fill((255, 248, 220))  # cream white
        pygame.draw.rect(screen, (0, 0, 0),
                         (220, 100, 200, 250))  # color black
        gameOver = self.bigfont.render("Game Over", True, (255, 97, 3))
        screen.blit(gameOver, (250, 130))
        points = self.font.render("Points: ", True, (255, 248, 220))
        screen.blit(points, (275, 175))
        time = self.font.render("Time: ", True, (255, 248, 220))
        screen.blit(time, (275, 215))
        highscore = self.font.render(
            "Highscore: ", True, (255, 248, 220))  # cream white
        # lisää highscore pisteet edelliseen
        screen.blit(highscore, (275, 255))
        playAgain = self.font.render(
            "Play Again", True, (255, 248, 220))  # cream white
        screen.blit(playAgain, (275, 295))
        # jos hiiri painaa nappia, uusi peli
        pygame.display.flip()
        # reset snake to original values in case of new game
        self.length = 1
        self.location = [(screenWidth/2), (screenHeight/2)]  # lista
        self.direction = random.choice([up, down, left, right])

class Food():
    def __init__(self):
        self.size = 8 # radius
        self.color = (139,69,19)
        self.location = (0,0)
        self.random_location()

    def random_location(self):
        self.location = (random.randint(0+self.size+3, 640-self.size-3), random.randint(5+self.size+3, 480-self.size-3))

    def draw_food(self):
        pygame.draw.circle(screen, self.color, self.location, self.size)

    # how often does food show up on screen
    #def frequency(self):
    #    pass

class Score():
    def __init__(self):
        self.points = 0
        self.count = 0

    #def eating(self):
    # check if snake and food collide and count food eaten
    #    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    x = (screenWidth/2)
    y = (screenHeight/2)
    clock = pygame.time.Clock()
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
        screen.fill((255, 248, 220))  # cream white
        Snake().draw_snake(x,y)
        pygame.display.flip()
        x += 1
        if x + 20 >= 640:
            break
        clock.tick(60)
    Snake().die()

main()

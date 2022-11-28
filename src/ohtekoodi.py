import random
import pygame

# Progress
# So far the short snake appears on screen and moves on it's own, but doesn't turn yet
# The snake dies when it hits the wall, but game over window doesn't stay on screen and instead disappears instantly

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
        self.location = [310, 230]  # lista

    def head_location(self):
        return self.location[0]  # width, so horizontal

    # def turn(self):
        # Jos käärme on vain 1 pituinen, se voi kääntyä mihin tahansa suuntaan. Jos se on isompi niin se voi kääntyä 3 suuntaan
        # eli ei ns taaksepäin, koska osa käärmeestä on jo takana eli se ei voi mennä itsensä päälle.
        # if self.length == 1:
        #    pass
        # else:
        #    pass

    # def grow(self):
    #    pass

    def draw_snake(self, x, y):
        # 20 is the size of the snake, x & y the location
        pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 20, 20))

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

# class Food():
#    def __init__():
#        pass

#    def location():
#        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    x = 310
    y = 230
    clock = pygame.time.Clock()
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
        screen.fill((255, 248, 220))  # cream white
        Snake().draw_snake(x, y)
        pygame.display.flip()
        x += 1
        if x + 20 >= 640:
            break
        clock.tick(60)
    Snake().die()


main()

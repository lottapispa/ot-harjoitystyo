import pygame
import random

# Write code in english!

screenWidth = 640
screenHeight = 480
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
        
class Snake():
    def __init__(self):
        self.length = 1
        self.color = (102, 205, 0) # green
        self.location = [(screenWidth/2), (screenHeight/2)] #lista
        self.direction = random.choice([up, down, left, right])
        self.snake = pygame.draw.rect((screenWidth, screenHeight), self.color, pygame.Rect(10, 10, 20, 20))

    #def head_location(self):
        #return self.location[0]

    #def turn(self):
        # Jos käärme on vain 1 pituinen, se voi kääntyä mihin tahansa suuntaan. Jos se on isompi niin se voi kääntyä 3 suuntaan 
        # eli ei ns taaksepäin, koska osa käärmeestä on jo takana eli se ei voi mennä itsensä päälle.
        #if self.length == 1:
        #    pass
        #else:
        #    pass

    #def grow(self):
    #    pass

    def die(self):
        pygame.init()
        self.font = pygame.font.SysFont("Candara" , 24)
        self.bigfont = pygame.font.SysFont("Candara" , 36)
        screen = pygame.display.set_mode((screenWidth, screenHeight))
        screen.fill((255,248,220)) # cream white
        pygame.draw.rect(screen, (0, 0, 0), (220, 100, 200, 250)) # color black
        gameOver = self.bigfont.render("Game Over", True, (255,97,3))
        screen.blit(gameOver, (250, 140))
        playAgain = self.font.render("Play Again", True, (255,248,220)) # cream white
        screen.blit(playAgain, (275, 200))
        # jos hiiri painaa nappia, uusi peli
        highscore = self.font.render("Highscore: ", True, (255,248,220)) # cream white
        # lisää highscore pisteet edelliseen
        screen.blit(highscore, (275, 250))
        pygame.display.flip()

#class Food():
#    def __init__():
#        pass

#    def location():
#        pass

def main(self):
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    snake = Snake().self.snake
    x, y = 0
    speed = 1
    clock = pygame.time.Clock()

    while True:
        for tapahtuma in pygame.event.get():
            screen.fill((255,248,220)) # cream white
            screen.blit(snake, (x, y))
            pygame.display.flip()
            x += speed
            if speed > 0 and x + snake.get_width() >= 640:
                Snake().die()
            if speed < 0 and x <= 0:
                Snake().die()
            clock.tick(60)
            if tapahtuma.type == pygame.QUIT:
                exit()
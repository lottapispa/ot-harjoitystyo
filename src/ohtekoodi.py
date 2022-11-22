import pygame
import random

# Write code in english!

# So far the short snake appears on screen, but doesn't move yet
# I've also been working on the game over window

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
        self.color = (102, 205, 0) # green
        self.location = [(screenWidth/2), (screenHeight/2)] #lista
        self.direction = random.choice([up, down, left, right])

    #def head_location(self):
        #return self.location[0]

    #def turn(self):
        # Jos käärme on vain 1 pituinen, se voi kääntyä mihin tahansa suuntaan. Jos se on isompi niin se voi kääntyä 3 suuntaan 
        # eli ei ns taaksepäin, koska osa käärmeestä on jo takana eli se ei voi mennä itsensä päälle.
        #if self.length == 1:
        #    pass
        #else:
        #    pass

    #def move(self):
    #    pass

    #def grow(self):
    #    pass

    def draw_snake(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(10, 10, 20, 20))

    def die(self):
        # reset snake to original values in case of new game
        self.length = 1
        self.location = [(screenWidth/2), (screenHeight/2)] #lista
        self.direction = random.choice([up, down, left, right])
        # Game over window
        pygame.init()
        self.font = pygame.font.SysFont("Candara" , 24)
        self.bigfont = pygame.font.SysFont("Candara" , 36)
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.screen.fill((255,248,220)) # cream white
        pygame.draw.rect(self.screen, (0, 0, 0), (220, 100, 200, 250)) # color black
        gameOver = self.bigfont.render("Game Over", True, (255,97,3))
        self.screen.blit(gameOver, (250, 140))
        playAgain = self.font.render("Play Again", True, (255,248,220)) # cream white
        self.screen.blit(playAgain, (275, 200))
        # jos hiiri painaa nappia, uusi peli
        highscore = self.font.render("Highscore: ", True, (255,248,220)) # cream white
        # lisää highscore pisteet edelliseen
        self.screen.blit(highscore, (275, 250))
        pygame.display.flip()

#class Food():
#    def __init__():
#        pass

#    def location():
#        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
        screen.fill((255,248,220)) # cream white
        Snake().draw_snake()
        pygame.display.flip()
        clock.tick(60)

main()
    
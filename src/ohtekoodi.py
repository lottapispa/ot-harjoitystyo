import pygame
import random

# Write code in english!

class Snake():
    def __init__(self):
        self.length = 1
        self.color = (102, 205, 0)
        self.location = [(screenWidth/2), (screenHeight/2)] #lista
        self.direction = random.choice([up, down, left, right])

    def head_location(self):
        return self.location[0]

    def turn(self):
        # Jos käärme on vain 1 pituinen, se voi kääntyä mihin tahansa suuntaan. Jos se on isompi niin se voi kääntyä 3 suuntaan 
        # eli ei ns taaksepäin, koska osa käärmeestä on jo takana eli se ei voi mennä itsensä päälle.
        if self.length == 1:
            pass
        else:
            pass

    def grow(self):
        pass

    def die(self):
        pass

class Food():
    def __init__():
        pass

    def location():
        pass

screenWidth = 640
screenHeight = 480
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    screen.fill((255,248,220))
    snake = Snake()
    food = Food()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
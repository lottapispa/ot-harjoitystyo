import pygame
import random

screenWidth = 640
screenHeight = 480
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
length = 1
color = (102, 205, 0) # green
location = [(screenWidth/2), (screenHeight/2)] #lista
direction = random.choice([up, down, left, right])
snake = pygame.draw.rect((screenWidth, screenHeight), color, pygame.Rect(10, 10, 20, 20))

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
x, y = 0
speed = 1
clock = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    screen.fill((255,248,220)) # cream white
    screen.blit(snake, (x, y))
    pygame.display.flip()
    clock.tick(60)
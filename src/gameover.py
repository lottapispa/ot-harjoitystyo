import pygame
import random

screenWidth = 640
screenHeight = 480

pygame.init()
font = pygame.font.SysFont("Candara" , 24)
bigfont = pygame.font.SysFont("Candara" , 36)
screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill((255,248,220))
pygame.draw.rect(screen, (0, 0, 0), (220, 100, 200, 220)) # color black
gameOver = bigfont.render("Game Over!", True, (255,97,3)) # cream white
screen.blit(gameOver, (250, 140))
playAgain = font.render("Play Again", True, (255,248,220)) # cream white
screen.blit(playAgain, (275, 200))
highscore = font.render("Highscore: ", True, (255,248,220)) # cream white
screen.blit(highscore, (275, 250))
pygame.display.flip()
while True:
    for tapahtuma in pygame.event.get():
        # if you press play again, game starts over
        #if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
        #    main()
        if tapahtuma.type == pygame.QUIT:
            exit()


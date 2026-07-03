from board import Board, BoardRenderer
from game import Game

import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()
running = True

board = Board()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    if event.type == pygame.MOUSEBUTTONDOWN:
        game.on_click(event.pos)

    game.draw(screen)            

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
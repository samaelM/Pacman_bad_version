import pygame
from Constants import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.posX = x
        self.posY = y
        self.image = pygame.image.load('Coin.png')
        self.image = pygame.transform.scale(self.image, (COIN_SIZE, COIN_SIZE))
        self.is_collected = 0

    def update(self, pacman):
        if abs(self.posX -  pacman.posX) <= (COIN_SIZE // 2 + PACMAN_SIZE // 2) and abs(self.posY -  pacman.posY) <= (COIN_SIZE // 2 + PACMAN_SIZE // 2):
            self.is_collected = 1
            pacman.score += 1

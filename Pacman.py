import pygame
from Constants import *

class Pacman():
    def __init__(self, x=0, y=0, speed=0):
        self.image = pygame.image.load('Pacman.png')
        self.image = pygame.transform.scale(self.image, (PACMAN_SIZE, PACMAN_SIZE))
        self.posX = x
        self.posY = y
        self.dX = 0
        self.dY = 0
        self.speed = speed
        self.score = 0
        self.is_alive = 1

    def death(self):
        self.image = pygame.image.load('Pacman_dead.png')
        self.image = pygame.transform.scale(self.image, (PACMAN_SIZE, PACMAN_SIZE))
        self.speed = 0
        self.dX = 0
        self.dY = 0
        self.is_alive = 0

    def update(self, walls):
        new_rect = self.image.get_rect().move(self.posX + self.dX, self.posY + self.dY)
        for wall in walls:
            if new_rect.colliderect(wall):
                self.dX = 0
                self.dY = 0
                break

        self.posX += self.dX
        self.posY += self.dY
        self.posX = max(0, min(self.posX, SCREEN_WIDTH - PACMAN_SIZE))
        self.posY = max(0, min(self.posY, SCREEN_HEIGHT - PACMAN_SIZE))

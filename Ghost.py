import pygame
from Constants import *

class Ghost():
    def __init__(self, x=0, y=0, speed=0):
        self.image = pygame.image.load('Ghost.png')
        self.image = pygame.transform.scale(self.image, (PACMAN_SIZE, PACMAN_SIZE))
        self.posX = x
        self.posY = y
        self.dX = 0
        self.dY = 0
        self.speed = speed
    
    def update(self, walls, pacman):
        self.dX = 0
        self.dY = 0
        if pacman.posX - self.posX > self.speed:
            self.dX = self.speed
        elif pacman.posX - self.posX < 0:
            self.dX = -self.speed
        else:
            self.dX = 0
        new_rect = self.image.get_rect().move(self.posX + self.dX, self.posY + self.dY)
        for wall in walls:
            if new_rect.colliderect(wall):
                self.dX = 0
                self.dY = 0
                break
        self.posX += self.dX
        self.dX = 0

        if pacman.posY - self.posY > self.speed:
            self.dY = self.speed
        elif pacman.posY - self.posY < 0:
            self.dY = -self.speed
        else:
            self.dY = 0
        new_rect = self.image.get_rect().move(self.posX + self.dX, self.posY + self.dY)
        for wall in walls:
            if new_rect.colliderect(wall):
                self.dX = 0
                self.dY = 0
                break
        self.posY += self.dY
        if abs(self.posX -  pacman.posX) <= (PACMAN_SIZE) and abs(self.posY -  pacman.posY) <= (PACMAN_SIZE):
            pacman.death()

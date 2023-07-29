import pygame
from Ghost import Ghost
from Constants import *
from Pacman import Pacman
from Coin import Coin

pygame.init()
pygame.font.init()

def draw_maze(screen):
    cell_width = SCREEN_WIDTH // GRID_WIDTH
    cell_height = SCREEN_HEIGHT // GRID_HEIGHT

    walls = []

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell_x = x * cell_width
            cell_y = y * cell_height

            if grid[y][x] == 1:
                pygame.draw.rect(screen, WALL_COLOR, (cell_x, cell_y, cell_width, cell_height))
                walls.append(pygame.Rect(cell_x, cell_y, cell_width, cell_height))
            else:
                pygame.draw.rect(screen, PATH_COLOR, (cell_x, cell_y, cell_width, cell_height))

    return walls
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pacman')

walls = []
coins = [
     Coin(100, 100),
     Coin(100, 200),
     Coin(300, 100),
     Coin(300, 200),
     Coin(300, 400)
]
ghosts = (Ghost(100, 100, 3))
pacman = Pacman(SCREEN_WIDTH // 2 - PACMAN_SIZE // 2, SCREEN_HEIGHT // 2 - PACMAN_SIZE // 2, PACMAN_SPEED)
font = pygame.font.Font(None, 36)
while True:
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                        pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman.dX = -pacman.speed
        pacman.dY = 0
    elif keys[pygame.K_RIGHT]:
        pacman.dX = pacman.speed
        pacman.dY = 0
    elif keys[pygame.K_UP]:
        pacman.dX = 0
        pacman.dY = -pacman.speed
    elif keys[pygame.K_DOWN]:
        pacman.dX = 0
        pacman.dY = pacman.speed
    elif keys[pygame.K_p]:
         pygame.quit()
    
    ghosts.update(walls, pacman)
    pacman.update(walls)
    walls = draw_maze(screen)
    screen.blit(pacman.image, (pacman.posX, pacman.posY))
    screen.blit(ghosts.image, (ghosts.posX, ghosts.posY))
    for c in coins:
        if c.is_collected:
              coins.pop(coins.index(c))
        else:
             c.update(pacman)
             screen.blit(c.image, (c.posX, c.posY))
    score_text = font.render("Score: " + str(pacman.score), True, WHITE)
    screen.blit(score_text, (10, 10))
    if pacman.score == 5:
        ghosts.speed = 0
        screen.fill(BLACK)
        win_text = font.render("Felicitation Vous avez gagnez! Appuyez sur p pour quitter", True, WHITE)
        screen.blit(win_text, (10, 10))
    if pacman.is_alive == 0:
        pygame.display.flip()
        pygame.time.delay(2000)
        screen.fill(BLACK)
        lose_text = font.render("T'es mort", True, WHITE)
        screen.blit(lose_text, (SCREEN_HEIGHT // 2, 10))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    pygame.display.flip()
    pygame.time.Clock().tick(30)

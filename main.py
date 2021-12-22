import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
surface = pygame.image.load("ufo.png")
pygame.display.set_icon(surface)

playerimg = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerimg, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print

    player(playerX, playerY)
    pygame.display.update()
